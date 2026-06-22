# AGENTS.md — Agent 工作指南

## 目录结构

```
profile/
├── AGENTS.md          # 本文件
├── README.md          # 仓库定位与目录说明
├── zed/
│   ├── AGENTS.md      # → ~/.config/zed/AGENTS.md
│   └── settings.json  # → ~/.config/zed/settings.json
├── opencode/
│   └── opencode.json  # → ~/.config/opencode/opencode.json
├── hermes/
│   └── config.yaml    # → ~/.hermes/config.yaml
```

## 维护规范

1. **以实际配置为准** — 从机器上的工作配置采集，不做设计
2. **cp 即用** — 文件放到目标路径即恢复配置，不做变量替换
3. **不重复维护可通过安装获取的内容** — 默认提示词、插件命令等由各自工具或仓库安装
