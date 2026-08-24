# 上下文（Contexts）

从实践对话中提取的**初步逻辑**记录。上下文工程的目的，是把原始对话整理为可复用的初步逻辑，并据此沉淀为 Skill 与 harness（见 [loops](../../default/loops/README.md)）。

与 loops 互补：loop 记录已封装的循环范式，context 记录某类任务**待封装**的初步逻辑——场景判定、命名逻辑、标准流程、决策规则与契约要求。

## 目录结构

仓库按**领域**为一级文件夹组织，未归入领域的通用内容存于 `default/`：

```text
profile/
├── default/               # 未分类的通用内容（agents/loops/skills/contexts）
└── <domain>/              # 领域一级文件夹，如 quanttide-asset/
    ├── contexts/          # 该领域的上下文（初步逻辑）
    └── sessions/          # 该领域的原始对话记录
```

本目录（`quanttide-asset/contexts/`）存放**资产领域**的上下文：

```text
quanttide-asset/
├── contexts/
│   ├── README.md
│   └── <上下文>.md   # 资产领域的上下文，如 second-brain-init
└── sessions/         # 原始对话，如 second-brain-init.jsonl
```

## 与 Skill / harness 的关系

上下文文档按 **原始对话 → 初步逻辑 → Skill/harness** 组织：

- **初步逻辑**：文档主体，可复用的规则与流程，各逻辑单元标注可沉淀的产出物
- **原始材料**：对话回合去敏索引，仅作回溯；原始对话存于同领域的 `sessions/`，不淹没逻辑本身
- **产出物清单**：由初步逻辑映射出的 Skill 与 harness 一览

## 目录

| 上下文 | 说明 |
|--------|------|
| [second-brain-init](second-brain-init.md) | 领域第二大脑初始化：新建/补全领域仓库、聚合容器的初步逻辑，可沉淀为命名助手 Skill 与第二大脑初始化 harness |

## 维护规范

1. **从实践提取** — 内容来自真实完成的初始化/维护实践，不是凭空设计
2. **先逻辑后原材料** — 以可复用逻辑为主体，原始对话仅作索引
3. **标注产物** — 各逻辑单元标注可沉淀的 Skill 与 harness，沉淀后回填产出物清单
4. **脱敏开源** — 仓库公开，不写入未公开的内部信息、个人数据与敏感细节
5. **与事实一致** — 命名、路径、流程必须与当前仓库结构对齐，随实践更新
