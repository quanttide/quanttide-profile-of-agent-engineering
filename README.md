# 智能体工程工作档案

跨 Agent 系统配置层。集中管理各 AI 编程工具的共享配置，新机器复制即可恢复。

## 定位

- **非代码仓库** — 只存 Agent 配置，不存应用代码
- **cp 即用** — 文件放到目标路径就可直接使用，不做变量替换或格式转换
- **以实际配置为准** — 从机器上的工作配置采集，非人工设计

## 目录结构

| 目录 | 对应工具 | 用途 | 恢复 |
|------|---------|------|------|
| `zed/` | Zed | 全局 AGENTS.md | `cp zed/AGENTS.md ~/.config/zed/AGENTS.md` |
| `opencode/command/` | OpenCode CLI | Ponytail 命令集 | `cp opencode/command/* ~/.config/opencode/command/` |

## 维护原则

- **以系统配置为准** — 改了机器配置就同步更新本仓库
- **发版后恢复** — 打 tag 发版，新机器拉取对应 tag 后 cp
