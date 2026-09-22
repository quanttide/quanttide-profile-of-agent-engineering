# Hermes 模型接入说明

## 配置位置

| 项 | 位置 | 是否入库 |
|------|------|---------|
| 模型选择 | `~/.hermes/config.yaml` 的 `model` 段 | 是（本目录 `config.yaml`） |
| API 密钥 | `~/.hermes/.env` | 否 |
| 模型列表缓存 | `~/.hermes/provider_models_cache.json`（1 小时 TTL） | 否 |

## model 段

```yaml
model:
  provider: deepseek
  default: deepseek-flash
  # base_url: 仅自定义 OpenAI 兼容端点需要；内置 provider 有默认值
```

- `provider` 用内置 provider id；常见别名会被归一化（`glm` / `z.ai` → `zai`，`mimo` → `xiaomi`，`kimi` / `moonshot` → `kimi-coding`）
- 当前默认：`deepseek` / `deepseek-flash`（DeepSeek V4.1 Flash）

## 常用 provider

| provider | 名称 | 内置 base URL | 密钥环境变量 |
|------|------|------|------|
| `deepseek` | DeepSeek | `https://api.deepseek.com/v1` | `DEEPSEEK_API_KEY` |
| `zai` | Z.AI / GLM | `https://api.z.ai/api/paas/v4` | `GLM_API_KEY`、`ZAI_API_KEY` |
| `xiaomi` | Xiaomi MiMo | `https://api.xiaomimimo.com/v1` | `XIAOMI_API_KEY` |
| `kimi-coding` | Kimi / Moonshot | `https://api.moonshot.ai/v1` | `KIMI_API_KEY` |

MiMo Token Plan 需自定义 `base_url: https://token-plan-cn.xiaomimimo.com/v1`，密钥为 `tp-` / `ttp-` 前缀。

## 切换模型

- 交互选择并刷新列表：`hermes model`（加 `--refresh` 清缓存、重拉各 provider 的 `/v1/models`）
- 改配置：`hermes config set model.provider zai`、`hermes config set model.default glm-5.3-flashx`
- 单次覆盖：`hermes -m mimo-v2.6-flash --provider xiaomi`
- 校验：`hermes config get model`、`hermes doctor`

## 模型列表来源

Hermes 不静态维护模型清单：选择器拉 provider 的 `/v1/models`，结果在 `provider_models_cache.json` 缓存 1 小时，新模型上线后刷新即可出现。live 拉取失败时回退到 `hermes_cli/models.py` 的静态兜底表，那部分要等 Hermes 发版。
