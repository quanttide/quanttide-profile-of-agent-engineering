# Zed Agent DeepSeek 配置说明

## 已配置的 DeepSeek 模型

Zed 1.19 内置原生 DeepSeek provider（`language_models.deepseek`），默认含以下模型；本目录另通过 `available_models` 追加了 V4.1 的规范模型名。

| 模型 | 来源 | 说明 |
|------|------|------|
| **deepseek-flash** | 手动追加 | 当前主力，DeepSeek-V4.1-Flash，1M 上下文 / 384K 输出，支持思考与图像 |
| `deepseek-v4-flash` | provider 内置 | 旧名，服务端路由到 V4.1 Flash，按 Flash 计费 |
| `deepseek-v4-pro` | provider 内置 | 旧名，2026-09-14 起服务端路由到 V4.1 Flash |

> 不新增 `openai_compatible` 条目——Zed 原生 provider 直接支持 DeepSeek，读取 `DEEPSEEK_API_KEY`，无需手填 `api_url`（默认 `https://api.deepseek.com/v1`）。

## API 配置

- **API 端点（原生默认）**: `https://api.deepseek.com/v1`
- **API 密钥获取**: https://platform.deepseek.com
- **API 文档**: https://api-docs.deepseek.com/zh-cn/

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://platform.deepseek.com 并登录
2. 创建 API 密钥

### 2. 在 Zed 中填写密钥

API 密钥不写入 `settings.json`，二选一：

- **环境变量**：`export DEEPSEEK_API_KEY=<密钥>` 后重启 Zed（由 provider ID 生成，优先级高于 keychain）
- **UI 方式（推荐）**：命令面板执行 `agent: open settings`，在 Settings → AI → LLM Providers 的 `DeepSeek` 部分填入密钥（存入系统 keychain）

### 3. 在 Agent 面板选择模型

配置生效后，在 Agent 面板模型选择器中选择 `DeepSeek → DeepSeek V4.1 Flash`（模型 ID `deepseek-flash`）。

当前主力模型即 `deepseek-flash`（`agent.default_model`，开启思考）。

## 配置详情

配置文件位置：

```
~/.config/zed/settings.json
```

配置结构（`language_models` → `deepseek`，与 `openai_compatible` 平级）：

```json
{
  "language_models": {
    "deepseek": {
      "available_models": [
        {
          "name": "deepseek-flash",
          "display_name": "DeepSeek V4.1 Flash",
          "max_tokens": 1000000,
          "max_output_tokens": 384000
        }
      ]
    }
  },
  "agent": {
    "default_model": {
      "provider": "deepseek",
      "model": "deepseek-flash",
      "enable_thinking": true
    }
  }
}
```

`DeepseekAvailableModel` 字段：`name`（必填）、`display_name`、`max_tokens`（上下文）、`max_output_tokens`（输出上限）。`available_models` 与内置模型合并，同名时覆盖内置项。

## 注意事项

1. **思考强度选择器不可用**：Zed 只对内置 V4 模型（`deepseek-v4-flash` / `deepseek-v4-pro`）开放 thinking/effort 控制；`deepseek-flash` 属自定义模型，面板不显示 effort。DeepSeek 服务端默认思考开启、`effort=high`，功能不受影响。需要手动调 effort 时临时切到内置 `deepseek-v4-flash`。
2. **密钥安全**：不要将 API 密钥提交到版本控制系统
3. **上下文缓存**：DeepSeek 服务端自动启用上下文硬盘缓存，无需额外配置

## 相关链接

- DeepSeek 开放平台: https://platform.deepseek.com
- DeepSeek API 文档: https://api-docs.deepseek.com/zh-cn/
- Zed OpenAI-compatible / 模型配置文档: https://zed.dev/docs/ai/use-api-access.html
