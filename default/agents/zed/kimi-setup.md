# Zed Agent Kimi 配置说明

## 已配置的 Kimi 模型

在 Zed 的 `settings.json` 中已添加以下 Kimi（Moonshot AI）模型：

| 模型 | 上下文 | 说明 |
|------|--------|------|
| **kimi-k3** | 1M | 旗舰模型，始终推理且保留式思考，支持视觉 |
| **kimi-k2.7-code** | 256K | Coding 模型，始终开启思考，支持文本/图片/视频 |
| **kimi-k2.7-code-highspeed** | 256K | 与 kimi-k2.7-code 同模型，输出速度约 5-6 倍 |
| **kimi-k2.6** | 256K | 通用思考模型，支持视觉与工具调用 |

> `kimi-k2.5`、`kimi-k2` 系列与 `moonshot-v1` 系列已于 2026 年下线，不再配置。

## API 配置

- **API 端点**: `https://api.moonshot.cn/v1`（开放平台 `platform.kimi.com` 的密钥；`platform.kimi.ai` 的国际站密钥不通用）
- **API 密钥获取**: https://platform.kimi.com/console/api-keys
- **Provider ID**: `Kimi` → 环境变量 `KIMI_API_KEY`

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://platform.kimi.com/ 并登录
2. 进入控制台 API Keys 页面创建密钥

### 2. 在 Zed 中填写密钥

API 密钥不写入 `settings.json`，二选一：

- **UI 方式（推荐）**：命令面板执行 `agent: open settings`，在 Settings → AI → LLM Providers 的 `Kimi` 部分填入密钥（存入系统 keychain）
- **环境变量**：设置 `KIMI_API_KEY=<密钥>` 后重启 Zed（优先级高于 keychain）

### 3. 在 Agent 面板选择模型

配置生效后，在 Agent 面板模型选择器中选择 `Kimi → Kimi K3` / `Kimi K2.7 Code` 等。

| 场景 | 推荐模型 |
|------|---------|
| 复杂推理、长上下文 | **Kimi K3** |
| 日常编码 | **Kimi K2.7 Code**（追求速度选 Highspeed） |
| 通用对话 | **Kimi K2.6** |

## 配置详情

配置文件位置：

```
~/.config/zed/settings.json
```

配置结构（`language_models` → `openai_compatible` → `Kimi`）：

```json
{
  "language_models": {
    "openai_compatible": {
      "Kimi": {
        "api_url": "https://api.moonshot.cn/v1",
        "available_models": [
          {
            "name": "kimi-k3",
            "display_name": "Kimi K3",
            "max_tokens": 1048576,
            "max_output_tokens": 131072,
            "max_completion_tokens": 131072,
            "reasoning_effort": "max",
            "capabilities": {
              "tools": true,
              "images": true,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": true,
              "max_tokens_parameter": false
            }
          },
          {
            "name": "kimi-k2.7-code",
            "display_name": "Kimi K2.7 Code",
            "max_tokens": 262144,
            "max_output_tokens": 32768,
            "max_completion_tokens": 32768,
            "capabilities": {
              "tools": true,
              "images": true,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": true,
              "max_tokens_parameter": false
            }
          }
        ]
      }
    }
  }
}
```

`api_url` 为 base URL，Zed 自动追加 `/chat/completions`。

## 注意事项

1. **思考强度**：仅 `kimi-k3` 支持 `reasoning_effort`（取值 `low` / `high` / `max`，默认 `max`）；K2.7 Code 与 K2.6 不支持该参数，故未配置——Zed 面板会列出 Minimal/Medium/Extra High 等档位，Kimi 只接受 low/high/max，K3 会话中不要选其他档位。切换档位会破坏前缀缓存命中，建议会话开始前定档。
2. **输出上限**：Kimi 已弃用 `max_tokens`（`max_tokens_parameter: false`，Zed 发送 `max_completion_tokens`）。K3 默认输出上限 131072（最大 1048576），K2.x 默认 32768；输入加输出超出上下文窗口会报 `invalid_request_error`，故不按上下文窗口写满。
3. **保留式思考**：`interleaved_reasoning: true` 使 Zed 把历史 `reasoning_content` 原样回传。K3 与 K2.7 Code 始终保留（K2.7 Code 为强制要求），K2.6 默认忽略历史思考，回传不影响单轮工具调用。
4. **固定参数**：全系列 `temperature` / `top_p` / `n` / `presence_penalty` / `frequency_penalty` 为固定值，显式传入其他值会报错，Zed 不传这些参数。
5. **多模态**：K3、K2.7 Code、K2.6 支持图片输入；视频仅支持文件上传，Zed 不发视频。
6. **密钥安全**：不要将 API 密钥提交到版本控制系统。

## 相关链接

- Kimi 开放平台: https://platform.kimi.com/
- 模型列表: https://platform.kimi.com/docs/models
- 模型参数参考: https://platform.kimi.com/docs/api/models-overview
- Zed OpenAI-compatible 配置文档: https://zed.dev/docs/ai/use-api-access.html
