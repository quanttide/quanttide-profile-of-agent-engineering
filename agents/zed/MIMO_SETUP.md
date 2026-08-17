# Zed Agent MiMo 配置说明

## 已配置的 MiMo 模型

在 Zed 的 `settings.json` 中已添加以下小米 MiMo 模型：

| 模型 | 说明 | 特点 |
|------|------|------|
| **MiMo-V2.5-Pro** | 专业版 | 高性能，支持工具调用 |
| **MiMo-V2.5-Flash** | 快速版 | 速度快，日常任务首选 |
| **MiMo-V2.5-Omni** | 全能版 | 支持图像，多模态 |

## API 配置

- **API 端点**: `https://api.xiaomimimo.com/v1`
- **API 密钥获取**: https://platform.xiaomimimo.com

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://platform.xiaomimimo.com
2. 注册/登录账号
3. 创建 API 密钥

### 2. 配置环境变量

在 `~/.hermes/hermes-agent/.env` 文件中添加：

```bash
XIAOMI_API_KEY=your_api_key_here
```

### 3. 在 Zed 中使用

1. 打开 Zed 编辑器
2. 打开命令面板（Ctrl+Shift+P / Cmd+Shift+P）
3. 搜索 "Assistant: Show Configuration" 或类似选项
4. 选择 MiMo 模型作为默认模型

### 4. 模型选择建议

根据选型报告的建议：

| 场景 | 推荐模型 |
|------|---------|
| 日常编码任务 | **MiMo-V2.5-Flash**（平价高效） |
| 复杂推理任务 | **MiMo-V2.5-Pro**（更强能力） |
| 多模态任务 | **MiMo-V2.5-Omni**（支持图像） |

## 配置详情

配置文件位置：
```
/home/iguo/repos/quanttide/domains/quanttide-agent/data/profile/agents/zed/settings.json
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
            "display_name": "MiMo-V2.5-Pro",
            "max_tokens": 128000,
            "max_output_tokens": 16384,
            "capabilities": {
              "tools": true,
              "images": false
            }
          },
          {
            "name": "mimo-v2.5-flash",
            "display_name": "MiMo-V2.5-Flash",
            "max_tokens": 128000,
            "max_output_tokens": 16384,
            "capabilities": {
              "tools": true,
              "images": false
            }
          },
          {
            "name": "mimo-v2.5-omni",
            "display_name": "MiMo-V2.5-Omni",
            "max_tokens": 128000,
            "max_output_tokens": 16384,
            "capabilities": {
              "tools": true,
              "images": true
            }
          }
        ]
      }
    }
  }
}
```

## 注意事项

1. **API 密钥安全**：不要将 API 密钥提交到版本控制系统
2. **费用控制**：MiMo 定价请参考官方文档
3. **模型选择**：Flash 版本更适合日常任务，Pro 版本适合复杂任务

## 相关链接

- MiMo 官网: https://mimo.xiaomi.com
- API 文档: https://platform.xiaomimimo.com
- Zed 配置文档: https://zed.dev/docs/configuring-zed