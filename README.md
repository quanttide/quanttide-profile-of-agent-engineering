# 量潮智能体工程档案

本仓库是**跨 Agent 系统配置层**。它集中管理各个 AI 编程工具（Zed、OpenCode、Hermes）的系统级规则、命令、插件，目标是一处维护、多机复用。


## 目录结构

仓库按**领域**为一级文件夹组织，未归入领域的通用内容存于 `default/`：

```
profile/
├── AGENTS.md          # 本文件
├── README.md          # 仓库定位与目录说明
├── default/           # 未分类的通用内容
│   ├── agents/        # 各 Agent 系统配置
│   │   ├── zed/               # → ~/.config/zed/
│   │   ├── opencode/          # → ~/.config/opencode/
│   │   ├── hermes/            # → ~/.hermes/
│   │   └── dsh/               # → DeepSeek Harness
│   ├── loops/         # 从实践日志提取的循环范式
│   │   ├── README.md
│   │   ├── devops-code/
│   │   └── devops-plan/
│   └── skills/        # 可安装技能（SKILL.md）
│       └── docs-format/
└── <domain>/          # 领域一级文件夹
    └── contexts/      # 该领域从实践对话提取的场景上下文
        └── README.md
```

## 维护规范

1. **以实际配置为准** — 本仓库的内容从机器上工作配置采集，而不是凭空设计
2. **cp 即用** — 文件放到目标路径就能恢复配置，不做变量替换或格式转换
