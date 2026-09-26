# Zed 配置文件

本目录维护 Zed 编辑器的系统配置，`cp` 到 `~/.config/zed/` 即可恢复。

> Ponytail 系统提示词由 ponytail 仓库统一管理（`AGENTS.md`），不作为副本在此维护。
> 新机器上需创建符号链接：`ln -s <ponytail-path>/AGENTS.md ~/.config/zed/AGENTS.md`

## 文件清单

| 文件 | 目标路径 | 说明 |
|---|---|---|
| `settings.json` | `~/.config/zed/settings.json` | 主配置 — 模型接入（z.ai GLM + DeepSeek + MiMo API / Token Plan + Kimi + StepFun）、Agent 工具权限、UI 主题字号 |
| `zai-setup.md` | — | z.ai（GLM 5.3 系列）接入配置方法 |
| `deepseek-setup.md` | — | DeepSeek（V4.1 Flash 等，原生 provider）接入配置方法 |
| `mimo-setup.md` | — | 小米 MiMo 接入配置方法 |
| `kimi-setup.md` | — | Kimi（K3 / K2.7 Code / K2.6）接入配置方法 |
| `stepfun-setup.md` | — | StepFun（Step 5 Preview / 3.7 Flash / 3.5 Flash）接入配置方法 |

> 完整配置参考见 `data/library/zed/config.md`。

## 关键配置项

- **主力模型**：MiMo 2.6 Flash（OpenAI-compatible `Xiaomi.MiMo.TokenPlan`，模型 ID `mimo-v2.6-flash`，1M 上下文 / 128K 输出，Token Plan 套餐）
- **备用模型**：MiMo 2.6 Pro / 2.5 Pro / 2.5（Token Plan 套餐 `Xiaomi.MiMo.TokenPlan`）、MiMo 2.6 Pro / 2.6 Pro UltraSpeed / 2.5 Pro / 2.5（按量付费 `Xiaomi.MiMo`）、GLM 5.3 / GLM 5.3 Flash / GLM 5.3 FlashX（z.ai，OpenAI-compatible）、DeepSeek V4.1 Flash / V4 Pro（原生 provider 内置）、Kimi K3 / K2.7 Code / K2.6（Kimi，OpenAI-compatible）、Step 5 Preview / Step 3.7 Flash / Step 3.5 Flash（StepFun，OpenAI-compatible）
- **工具权限**：`write_file`、`edit_file` 等已配置 always_allow 路径白名单
- **主题**：跟随系统（深色 One Dark / 浅色 One Light）
- **字号**：UI 16px / 编辑器 15px
