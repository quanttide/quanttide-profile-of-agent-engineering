# 循环（Loops）

从实践日志（journal）中提取的**循环范式**记录。档案记录的就是各种 harness 的技巧、循环、约束，其中循环是最核心的形态。

## Loop 范式

> 先从人类的视角出发，然后再回到人类的视角，中间把复杂的部分交给机器自己去做。

## Loop 与 Workflow 的区别

- **workflow** 单次就能做完，处理不了动态的情况
- **loop** 的关键是**反馈点**——一次循环过后需要与人交互一下，然后再进行下一次循环
- 很多情况像 workflow，但需要知道循环的反馈点在哪里，这正是 loop 区别于 workflow 的地方

## 承载方式

- 一个 loop 需要一个流程来承载，哪怕只是一个简单的 SH 脚本或 Python 脚本
- 本仓库用 **YAML 定义 steps**（见 [devops-code/specification.yaml](devops-code/specification.yaml)、[devops-plan/specification.yaml](devops-plan/specification.yaml)），展示性与结构化优于脚本，比 Markdown 更适合程序读取
- 可以用 Markdown 把 harness 写成 loop，叫 loop engineering
- 需要在 PI 的基础上进行封装

## 目录

| 循环 | 说明 | 定义 | 实现 |
|------|------|------|------|
| [devops-code](devops-code/requirement.md) | 开发循环：文档驱动 + 测试驱动 + 评审重构 | [specification.yaml](devops-code/specification.yaml) | [implementation.py](devops-code/implementation.py) |
| [devops-plan](devops-plan/requirement.md) | 规划循环：intention → insights → roadmap | [specification.yaml](devops-plan/specification.yaml) | — |

## 验证

### 验证范式

> loop 是数据处理流水线——一步一步按照这个来，收结果。

验证 = 逐站检查产物 + 反馈点检查 + 度量指标对比。

### 反馈点检查

- 一轮结束后**必须**向人类呈现结果并等待判断，人未参与的轮次视为失效
- 连续多轮无人交互 = 退化为 workflow，loop 定义失效

### 度量指标

每个任务记录：

| 指标 | 说明 | 有效阈值（试点后校准） |
|------|------|----------------------|
| 轮次 | 完成一轮任务的循环次数 | 待校准 |
| 耗时 | 人 + 机总耗时 | 待校准 |
| 纠偏次数 | 人修正 AI 产物的次数 | 待校准 |
| 返工率 | 因偏差重做的阶段数 / 总阶段数 | 待校准 |

> 校准方法：真实试点后，与"不跑 loop"的基线对比填写阈值。

### 有效性判定

一个 loop 有效，当且仅当：

1. 一轮跑完所有阶段产物齐备且达标
2. 反馈点真实触发（人参与判断）
3. 相同任务重复 2 次结果稳定
4. 人的成本（耗时/纠偏/返工）不高于基线

### 执行方式

- 产物断言由承载脚本 `--check` 自动执行，人工复核反馈点与偏差记录
- 试点与对比结果记录在 `trials/` 下

### Loop 定义

YAML 定义包含完整的循环结构：`entry`/`exit`（人类视角起止）、`steps`（每步含 actor / artifact / check）、`feedback`（反馈点）、`loop`（重跑与退出条件）、`metrics`（度量指标）。

- [devops-code/specification.yaml](devops-code/specification.yaml) — 开发循环定义
- [devops-plan/specification.yaml](devops-plan/specification.yaml) — 规划循环定义
- [devops-code/implementation.py](devops-code/implementation.py) — 基于 LangGraph 的循环智能体实现（读取 specification.yaml 执行，human 步骤与反馈点 interrupt 等人）
