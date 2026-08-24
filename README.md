# 量潮智能体工程档案

本仓库是**跨 Agent 系统配置层**。它集中管理各个 AI 编程工具（Zed、OpenCode、Hermes）的系统级规则、命令、插件，目标是一处维护、多机复用。


## 目录结构

```
profile/
├── AGENTS.md          # 本文件
├── README.md          # 仓库定位与目录说明
└── agents/            # 各 Agent 系统配置
    ├── zed/
    │   ├── AGENTS.md          # → ~/.config/zed/AGENTS.md
    │   ├── settings.json      # → ~/.config/zed/settings.json
    │   └── README.md          # zed 配置说明
    ├── opencode/
    │   ├── opencode.json      # → ~/.config/opencode/opencode.json
    │   └── README.md          # opencode 配置说明
    └── hermes/
        ├── config.yaml        # → ~/.hermes/config.yaml
        └── README.md          # hermes 配置说明
└── loops/              # 从实践日志提取的循环范式
    ├── README.md             # loop 概念与范式
    ├── devops-code.md         # 开发循环
    └── devops-plan.md         # 规划循环
└── contexts/           # 从实践对话提取的场景上下文
    ├── README.md             # 上下文概念与维护规范
    └── asset-init.md         # 资产初始化场景（新建/补全领域仓库与聚合容器）
└── skills/             # 可安装技能（SKILL.md）
    └── docs-format/
        └── SKILL.md          # 文档格式技能，依据《量潮科技文档格式章程》
```

## 维护规范

1. **以实际配置为准** — 本仓库的内容从机器上工作配置采集，而不是凭空设计
2. **cp 即用** — 文件放到目标路径就能恢复配置，不做变量替换或格式转换
