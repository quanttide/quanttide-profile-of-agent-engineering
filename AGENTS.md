# AGENTS.md — Agent 工作指南

## 仓库定位

本仓库是**跨 Agent 系统配置层**。它集中管理各个 AI 编程工具（Zed、OpenCode、Hermes）的系统级规则、命令、插件，目标是一处维护、多机复用。

## 目录结构

```
profile/
├── AGENTS.md          # 本文件
├── README.md          # 仓库定位与目录说明
├── zed/
│   ├── AGENTS.md      # → ~/.config/zed/AGENTS.md
│   └── settings.json  # Zed settings.json 配置参考
├── opencode/
│   ├── opencode.json  # → ~/.config/opencode/opencode.json 配置参考
│   └── command/       # Ponytail 命令（→ ~/.config/opencode/command/）
└── hermes/
    └── README.md      # Hermes 插件与 skills 引用说明
```

## 维护规范

1. **以实际配置为准** — 本仓库的内容从机器上工作配置采集，而不是凭空设计
2. **更新原则**：改机器配置 → 同步更新本仓库 → 发版
3. **新机器配置**：拉取本仓库 → 按各目录说明将文件复制/安装到对应位置

> ponytail: 最小骨架起步，缺的 Agent 配置按需追加，不预设未来需求。
