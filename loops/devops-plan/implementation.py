#!/usr/bin/env python3
"""devops-code 循环智能体——基于 specification.yaml 的 LangGraph 实现。

读取同目录 specification.yaml（loop 定义），构建 LangGraph：
  steps 串联 → feedback 反馈点（interrupt 等人类）→ redo 回环 / exit 退出

用法：
  python implementation.py <任务目录> [--task "任务描述"] [--dry-run]

LLM 配置（DeepSeek，OpenAI 兼容）：
  DEEPSEEK_API_KEY   必需（未设置时尝试读取 ~/.hermes/.env）
  DEEPSEEK_BASE_URL  默认 https://api.deepseek.com
  DEEPSEEK_MODEL     默认 deepseek-chat
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import TypedDict

import yaml
from openai import OpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt
from langgraph.checkpoint.memory import MemorySaver

SPEC_FILE = Path(__file__).parent / "specification.yaml"
ARTIFACT_STEP_FILE = "step-{n}-{name}.md"  # 目录型产物的文件名模板


# ---------- State ----------

class LoopState(TypedDict, total=False):
    task: str               # 任务描述
    task_dir: str           # 任务目录
    round: int              # 循环轮次
    artifacts: dict         # step 名 -> 产物路径
    history: list           # 各轮人类反馈记录


# ---------- LLM ----------

def load_env() -> None:
    """未设置 DEEPSEEK_API_KEY 时从 ~/.hermes/.env 加载。"""
    if os.environ.get("DEEPSEEK_API_KEY"):
        return
    env_file = Path.home() / ".hermes" / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                if k.strip() == "DEEPSEEK_API_KEY":
                    os.environ["DEEPSEEK_API_KEY"] = v.strip().strip('"')


def make_client() -> OpenAI:
    load_env()
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        sys.exit("缺少 DEEPSEEK_API_KEY（可设置环境变量或在 ~/.hermes/.env 中配置）")
    return OpenAI(
        api_key=key,
        base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
    )


# ---------- 图节点 ----------

class LoopAgent:
    def __init__(self, spec: dict, client: OpenAI):
        self.spec = spec
        self.client = client
        self.model = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")
        self.steps = spec["steps"]
        self.feedback_spec = spec.get("feedback", [])
        self.metrics = {"rounds": 0, "corrections": 0, "start": time.time()}

    # -- 产物写入 --

    def write_artifact(self, step: dict, content: str, task_dir: Path) -> str:
        """按 artifact 字段写入产物：目录型（docs/）或文件型（review.md）。"""
        artifact = step.get("artifact", "")
        if not artifact:
            return ""
        path = task_dir / artifact
        if artifact.endswith("/"):
            path.mkdir(parents=True, exist_ok=True)
            path = path / ARTIFACT_STEP_FILE.format(n=step.get("n", 0), name=step["name"])
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return str(path)

    # -- AI 步骤 --

    def ai_step(self, step: dict, state: LoopState) -> LoopState:
        task_dir = Path(state["task_dir"])
        prompt = self.build_prompt(step, state)
        content = self.llm(prompt)
        path = self.write_artifact(step, content, task_dir)
        return {"artifacts": {**state.get("artifacts", {}), step["name"]: path}}

    def build_prompt(self, step: dict, state: LoopState) -> str:
        return f"""你正在执行「{self.spec['name']}」循环的一个步骤。

循环说明：{self.spec['description']}
任务：{state['task']}
当前步骤：{step['name']}
步骤要求：{step.get('note', '')}
达标标准：{step.get('check', '')}
已完成的产物：{json.dumps(state.get('artifacts', {}), ensure_ascii=False)}

请直接输出本步骤的产物内容（Markdown）。"""

    def llm(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是量潮智能体工程循环的执行者，输出简洁、可落地的产物。"},
                {"role": "user", "content": prompt},
            ],
        )
        return resp.choices[0].message.content or ""

    # -- 图构建 --

    def build(self):
        return self._build_graph().compile(checkpointer=MemorySaver())

    def _build_graph(self):
        g = StateGraph(LoopState)

        # 每个 step 一个节点；human / human+ai 步骤挂起等人
        for i, step in enumerate(self.steps):
            step["n"] = i + 1
            if step.get("actor") == "human":
                def node(state, step=step):
                    answer = interrupt({
                        "ask": f"人类步骤：{step['name']}（{step.get('note', '')}）\n请完成并输入产物内容或路径：",
                    })
                    path = self.write_artifact(step, str(answer), Path(state["task_dir"]))
                    return {"artifacts": {**state.get("artifacts", {}), step["name"]: path}}
            elif step.get("actor") == "human+ai":
                def node(state, step=step):
                    task_dir = Path(state["task_dir"])
                    draft = self.llm(self.build_prompt(step, state))
                    path = self.write_artifact(step, draft, task_dir)
                    comment = interrupt({
                        "ask": f"AI 已生成 {step['name']}（{path}）。请评审：输入意见（追加）或 ok（通过）：",
                    })
                    if str(comment).strip().lower() not in ("ok", "通过", ""):
                        self.metrics["corrections"] += 1
                        draft = draft + f"\n\n## 人类评审意见\n{comment}"
                        path = self.write_artifact(step, draft, task_dir)
                    return {"artifacts": {**state.get("artifacts", {}), step["name"]: path}}
            else:
                def node(state, step=step):
                    return self.ai_step(step, state)
            step["_node"] = f"step_{i}"
            g.add_node(f"step_{i}", node)

        # 反馈点节点：一轮结束后停下，问人类是否重做或退出
        def feedback_node(state: LoopState):
            ask = self.feedback_spec[0]["ask"] if self.feedback_spec else "本轮完成。继续（重做）还是退出？"
            answer = interrupt({"ask": ask, "artifacts": state.get("artifacts", {})})
            # 注意：interrupt 之前的副作用会被重放两次，计数必须放在 interrupt 之后
            self.metrics["rounds"] += 1
            text = str(answer).strip().lower()
            if text in ("exit", "ok", "done", "退出", "确认", ""):
                return Command(goto=END, update={"history": state.get("history", []) + [str(answer)]})
            # redo <步骤名或编号>：回到对应步骤；否则从头重跑
            target = str(answer).strip()
            for s in self.steps:
                if target in (s["name"], str(s["n"])):
                    self.metrics["corrections"] += 1
                    return Command(goto=s["_node"], update={
                        "round": state.get("round", 0) + 1,
                        "history": state.get("history", []) + [str(answer)],
                    })
            self.metrics["corrections"] += 1
            return Command(goto=self.steps[0]["_node"], update={
                "round": state.get("round", 0) + 1,
                "history": state.get("history", []) + [str(answer)],
            })

        g.add_node("feedback", feedback_node)

        # 串联：START → step1 → ... → stepN → feedback
        prev = START
        for s in self.steps:
            g.add_edge(prev, s["_node"])
            prev = s["_node"]
        g.add_edge(prev, "feedback")

        return g

    # -- 运行 --

    def run(self, initial: LoopState):
        graph = self.build()
        config = {"configurable": {"thread_id": "devops-plan-loop"}}
        state: object = initial
        while True:
            interrupted = False
            for chunk in graph.stream(state, config, stream_mode="updates"):
                for node, update in chunk.items():
                    if node == "__interrupt__":
                        interrupted = True
                        for it in update:
                            self.present(it.value)
                        answer = input("> ").strip()
                        state = Command(resume=answer)
            if not interrupted:
                break
        return graph.get_state(config).values

    def present(self, value: object) -> None:
        """展示 interrupt 内容并请求输入。"""
        if isinstance(value, dict):
            print("\n——", value.get("ask", "请确认"), "——")
            arts = value.get("artifacts")
            if arts:
                print("本轮产物：")
                for name, path in arts.items():
                    print(f"  {name}: {path}")
        else:
            print("\n——", value, "——")


def main():
    ap = argparse.ArgumentParser(description="devops-code 循环智能体")
    ap.add_argument("task_dir", help="任务目录（产物将写入其中）")
    ap.add_argument("--task", default="", help="任务描述（缺省读取 <任务目录>/task.md）")
    ap.add_argument("--dry-run", action="store_true", help="只打印循环计划，不执行")
    args = ap.parse_args()

    spec = yaml.safe_load(SPEC_FILE.read_text(encoding="utf-8"))
    task_dir = Path(args.task_dir).resolve()
    task_dir.mkdir(parents=True, exist_ok=True)

    task = args.task
    if not task:
        task_file = task_dir / "task.md"
        task = task_file.read_text(encoding="utf-8") if task_file.exists() else "(未提供任务描述)"

    print(f"== {spec['name']}：{spec['description']} ==")
    print(f"入口：{spec['entry']}")
    for i, s in enumerate(spec["steps"], 1):
        print(f"  {i}. [{s.get('actor', 'ai')}] {s['name']} → {s.get('artifact', '-')}")
    print(f"出口：{spec['exit']}")

    if args.dry_run:
        print("\n[dry-run] 仅预览，不执行。")
        return

    agent = LoopAgent(spec, make_client())
    result = agent.run({
        "task": task,
        "task_dir": str(task_dir),
        "round": 0,
        "artifacts": {},
        "history": [],
    })
    elapsed = time.time() - agent.metrics["start"]
    print(f"\n== 循环结束：rounds={agent.metrics['rounds']}, corrections={agent.metrics['corrections']}, 耗时={elapsed:.1f}s ==")
    print("产物：")
    for name, path in (result or {}).get("artifacts", {}).items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main()
