# Zed Agent MiMo 配置说明

## 已配置的 MiMo 模型

在 Zed 的 `settings.json` 中已添加以下小米 MiMo 模型：

| 模型 | 说明 | 特点 |
|------|------|------|
| **mimo-v2.5-pro** | 专业版 | 高性能，支持工具调用 |
| **mimo-v2.5** | 全能版 | 支持图像，多模态 |

## API 配置

- **API 端点**: `https://api.xiaomimimo.com/v1`
- **API 密钥获取**: https://platform.xiaomimimo.com

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://platform.xiaomimimo.com
2. 注册/登录账号
3. 创建 API 密钥

### 2. 在 Zed 中使用

1. 打开 Zed 编辑器
2. 打开设置（Settings），在 `language_models` → `openai_compatible` → `Xiaomi.MiMo` 下填写 API 密钥
3. 在 Agent 面板的模型选择器中选择 MiMo 模型作为默认模型

### 3. 模型选择建议

| 场景 | 推荐模型 |
|------|---------|
| 日常编码任务 | **mimo-v2.5**（支持图像，多模态） |
| 复杂推理任务 | **mimo-v2.5-pro**（更强能力） |

## 配置详情

配置文件位置：
```
~/.config/zed/settings.json
```

配置结构：
```json
{
  "language_models": {
    "openai_compatible": {
      "Xiaomi.MiMo": {
        "api_url": "https://api.xiaomimimo.com/v1",
        "available_models": [
          {
            "name": "mimo-v2.5-pro",
            "display_name": "Mimo 2.5 Pro",
            "max_tokens": 128000,
            "max_output_tokens": 16384,
            "max_completion_tokens": 16384,
            "capabilities": {
              "tools": true,
              "images": false,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": false
            }
          },
          {
            "name": "mimo-v2.5",
            "display_name": "Mimo 2.5",
            "max_tokens": 128000,
            "max_output_tokens": 16384,
            "max_completion_tokens": 16384,
            "capabilities": {
              "tools": true,
              "images": true,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": false
            }
          }
        ]
      }
    }
  },
  "agent": {
    "default_model": {
      "provider": "Xiaomi.MiMo",
      "model": "mimo-v2.5",
      "enable_thinking": false
    }
  }
}
```

## 注意事项

1. **API 密钥安全**：不要将 API 密钥提交到版本控制系统
2. **费用控制**：MiMo 定价请参考官方文档
3. **模型选择**：默认模型为 mimo-v2.5（`enable_thinking: false`）

## 相关链接

- MiMo 官网: https://mimo.xiaomi.com
- API 文档: https://platform.xiaomimimo.com
- Zed 配置文档: https://zed.dev/docs/configuring-zed
