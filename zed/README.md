# Zed 配置文件

本目录维护 Zed 编辑器的系统配置，`cp` 到 `~/.config/zed/` 即可恢复。

> Ponytail 系统提示词由 ponytail 仓库统一管理（`AGENTS.md`），不作为副本在此维护。
> 新机器上需创建符号链接：`ln -s <ponytail-path>/AGENTS.md ~/.config/zed/AGENTS.md`

## 文件清单

| 文件 | 目标路径 | 说明 |
|---|---|---|
| `settings.json` | `~/.config/zed/settings.json` | 主配置 — 模型接入（DeepSeek + GLM）、Agent 工具权限、UI 主题字号 |

> 完整配置参考见 `data/library/zed/config.md`。

## 关键配置项

- **主力模型**：DeepSeek V4 Flash（高努力模式，开启思考）
- **备用模型**：GLM-5.2 / GLM-5V-Turbo（智谱 OpenAI-compatible）
- **工具权限**：`write_file`、`edit_file` 等已配置 always_allow 路径白名单
- **主题**：跟随系统（深色 One Dark / 浅色 One Light）
- **字号**：UI 16px / 编辑器 15px
