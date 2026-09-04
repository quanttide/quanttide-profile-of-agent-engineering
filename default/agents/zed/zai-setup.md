# Zed Agent z.ai 配置说明

## 已配置的 z.ai 模型

在 Zed 的 `settings.json` 中已添加以下智谱 z.ai 模型（GLM 5.3 系列）：

| 模型 | 说明 | 特点 |
|------|------|------|
| **glm-5.3** | 旗舰版 | 1M 上下文 / 128K 输出，纯文本，强制开启思考 |
| **glm-5.3-flash** | 快速版 | 1M 上下文 / 128K 输出，支持图像输入（多模态） |

## API 配置

- **API 端点**: `https://api.z.ai/api/paas/v4`（按量付费）
- **Coding Plan 端点**: `https://api.z.ai/api/coding/paas/v4`（GLM Coding Plan 订阅用户须改用此端点）
- **API 密钥获取**: https://z.ai 控制台

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://z.ai 并登录控制台
2. 创建 API 密钥

### 2. 在 Zed 中填写密钥

API 密钥不写入 `settings.json`，二选一：

- **UI 方式（推荐）**：命令面板执行 `agent: open settings`，在 Settings → AI → LLM Providers 的 `zai` 部分填入密钥（存入系统 keychain）
- **环境变量**：设置 `ZAI_API_KEY=<密钥>` 后重启 Zed（环境变量由 provider ID 生成，优先级高于 keychain）

### 3. 在 Agent 面板选择模型

配置生效后，在 Agent 面板模型选择器中选择 `zai → GLM 5.3` 或 `GLM 5.3 Flash`。

当前主力模型为 **GLM 5.3 Flash**（`agent.default_model`，高努力模式，开启思考）。

## 配置详情

配置文件位置：

```
~/.config/zed/settings.json
```

配置结构（`language_models` → `openai_compatible` → `zai`）：

```json
{
  "language_models": {
    "openai_compatible": {
      "zai": {
        "api_url": "https://api.z.ai/api/paas/v4",
        "available_models": [
          {
            "name": "glm-5.3",
            "display_name": "GLM 5.3",
            "max_tokens": 1000000,
            "max_output_tokens": 128000,
            "max_completion_tokens": 128000,
            "reasoning_effort": "high",
            "capabilities": {
              "tools": true,
              "images": false,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": false,
              "max_tokens_parameter": true
            }
          },
          {
            "name": "glm-5.3-flash",
            "display_name": "GLM 5.3 Flash",
            "max_tokens": 1000000,
            "max_output_tokens": 128000,
            "max_completion_tokens": 128000,
            "reasoning_effort": "max",
            "capabilities": {
              "tools": true,
              "images": true,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": false,
              "max_tokens_parameter": true
            }
          }
        ]
      }
    }
  }
}
```

关键 capabilities 说明：

- `chat_completions: true`：走 OpenAI Chat Completion 协议
- `max_tokens_parameter: true`：输出上限以 `max_tokens` 参数发送（GLM 不用 `max_completion_tokens`）
- `reasoning_effort`：思考强度，GLM 支持 `low` / `high` / `max`

## 注意事项

1. **GLM-5.3 强制开启思考**：不可关闭，思考强度可在 Agent 面板模型选择处调整
2. **Coding Plan 订阅用户**：只能走 `https://api.z.ai/api/coding/paas/v4`，否则请求失败
3. **排错**：若调用报 `interleaved_reasoning` 相关错误，将 `capabilities.interleaved_reasoning` 改为 `true` 重试
4. **密钥安全**：不要将 API 密钥提交到版本控制系统

## 相关链接

- z.ai 官网: https://z.ai
- GLM-5.3 模型文档: https://docs.z.ai/guides/llm/glm-5.3
- Zed OpenAI-compatible 配置文档: https://zed.dev/docs/ai/use-api-access.html（OpenAI-Compatible Endpoints 一节）
