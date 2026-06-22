# AGENTS.md — Agent 工作指南

## 仓库定位

本仓库是**跨 Agent 系统配置层**。它集中管理各个 AI 编程工具（Zed、OpenCode、Hermes）的系统级规则、命令、插件，目标是一处维护、多机复用。

## 目录结构

```
profile/
├── AGENTS.md          # 本文件
├── README.md          # 仓库定位与目录说明
├── zed/
│   └── AGENTS.md      # → ~/.config/zed/AGENTS.md
└── opencode/
    └── command/       # Ponytail 命令（→ ~/.config/opencode/command/）
```

## 维护规范

1. **以实际配置为准** — 本仓库的内容从机器上工作配置采集，而不是凭空设计
2. **cp 即用** — 文件放到目标路径就能恢复配置，不做变量替换或格式转换
3. **新机器**：拉本仓库 → `cp` 各文件到对应路径

> ponytail: 最小骨架起步，缺的 Agent 配置按需追加，不预设未来需求。
