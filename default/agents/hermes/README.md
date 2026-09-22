# Hermes 配置

| 文件 | 目标路径 | 说明 |
|---|---|---|
| `config.yaml` | `~/.hermes/config.yaml` | 运行时配置（模型、stt、voice、审批等，仅记非默认值） |
| `model-setup.md` | — | 模型接入配置方法（provider / 密钥 / 切换与刷新） |

> `.env` 含 API 密钥不纳入版本管理，`SOUL.md` 为默认系统提示词（安装可得），均不在此维护。
> 完整配置参考见 `data/library/hermes/config.md`。

## 关键配置项

- **默认模型**：`deepseek` / `deepseek-flash`（DeepSeek V4.1 Flash，读 `DEEPSEEK_API_KEY`）
- **备用 provider**：zai（GLM 5.3 系列）、xiaomi（MiMo 2.6 系列）、kimi-coding 等，见 `model-setup.md`
- **模型列表**：不静态维护，运行时拉 provider 的 `/v1/models` 并缓存 1 小时
- **STT**：Groq（`GROQ_API_KEY`），`language: zh`
- **审批**：`destructive_slash_confirm: false`；`agent.max_turns: 150`
