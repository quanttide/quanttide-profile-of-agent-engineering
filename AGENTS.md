# AGENTS.md — Agent 工作指南

## 目录结构

仓库按**领域**为一级文件夹组织，未归入领域的通用内容存于 `default/`：

```
profile/
├── AGENTS.md          # 本文件
├── README.md          # 仓库定位与目录说明
├── default/           # 未分类的通用内容
│   ├── agents/        # 各 Agent 系统配置
│   │   ├── zed/       # → ~/.config/zed/
│   │   ├── opencode/  # → ~/.config/opencode/
│   │   ├── hermes/    # → ~/.hermes/
│   │   └── dsh/       # → DeepSeek Harness
│   ├── loops/         # 从实践日志提取的循环范式
│   │   ├── README.md
│   │   ├── devops-code/
│   │   └── devops-plan/
│   └── skills/        # 可安装技能（SKILL.md）
│       └── docs-format/
└── <domain>/          # 领域一级文件夹
    └── contexts/      # 该领域的场景上下文
```

## 维护规范

1. **以实际配置为准** — 从机器上的工作配置采集，不做设计
2. **cp 即用** — 文件放到目标路径即恢复配置，不做变量替换
3. **不重复维护可通过安装获取的内容** — 默认提示词、插件命令等由各自工具或仓库安装
