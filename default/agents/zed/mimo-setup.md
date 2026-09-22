# Zed Agent MiMo 配置说明

## 已配置的 MiMo 模型

在 Zed 的 `settings.json` 中已添加以下小米 MiMo 模型：

| 模型 | 说明 | 特点 |
|------|------|------|
| **mimo-v2.6-pro** | 专业版 | 1M 上下文 / 128K 输出，全模态，深度思考 |
| **mimo-v2.6-flash** | 快速版 | 同上，单价更低，适合高频调用 |
| **mimo-v2.6-pro-ultraspeed** | 超速版 | 同上，面向实时交互，单价最高 |
| **mimo-v2.5-pro** | 旧版专业版 | 2026-10-21 下线，仅作过渡 |
| **mimo-v2.5** | 旧版全能版 | 2026-10-21 下线，仅作过渡 |

## API 配置

- **API 端点（按量付费）**: `https://api.xiaomimimo.com/v1`
- **API 端点（Token Plan 套餐）**: `https://token-plan-cn.xiaomimimo.com/v1`
- **API 密钥获取**: https://platform.xiaomimimo.com

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://platform.xiaomimimo.com
2. 注册/登录账号
3. 创建 API 密钥（按量付费为 `sk-` 前缀，Token Plan 为 `tp-` / `ttp-` 前缀）

### 2. 在 Zed 中使用

1. 打开 Zed 编辑器
2. 打开设置（Settings），在 `language_models` → `openai_compatible` → `Xiaomi.MiMo` 下填写 API 密钥
3. 在 Agent 面板的模型选择器中选择 MiMo 模型作为默认模型

### 3. 模型选择建议

| 场景 | 推荐模型 |
|------|---------|
| 复杂项目、长程任务、高价值工作 | **mimo-v2.6-pro** |
| 专业办公场景的高频调用、批量化任务 | **mimo-v2.6-flash** |
| 强调实时交互、对响应速度敏感的生产场景 | **mimo-v2.6-pro-ultraspeed** |

## 配置详情

配置文件位置：
```
~/.config/zed/settings.json
```

配置结构（`available_models` 片段，模型按从新到旧排列）：
```json
{
  "language_models": {
    "openai_compatible": {
      "Xiaomi.MiMo": {
        "api_url": "https://api.xiaomimimo.com/v1",
        "available_models": [
          {
            "name": "mimo-v2.6-pro",
            "display_name": "MiMo 2.6 Pro",
            "max_tokens": 1048576,
            "max_output_tokens": 131072,
            "max_completion_tokens": 131072,
            "capabilities": {
              "tools": true,
              "images": true,
              "parallel_tool_calls": false,
              "prompt_cache_key": false,
              "chat_completions": true,
              "interleaved_reasoning": true
            }
          }
        ]
      }
    }
  }
}
```

三个 2.6 模型的能力位与长度限制相同，仅 `name` / `display_name` 不同。

## 注意事项

1. **API 密钥安全**：不要将 API 密钥提交到版本控制系统
2. **参数限制**：思考模式下 `temperature`、`top_p` 不可自定义，服务端强制为 `1.0` / `0.95`
3. **思考回传**：MiMo 的思考内容走 `reasoning_content` 字段，多轮工具调用若缺少历史 `reasoning_content` 会损失上下文、降低指令遵循度；因此 `capabilities.interleaved_reasoning` 必须为 `true`（Zed 据此把历史思考原样回传）
4. **旧版下线**：`mimo-v2.5-pro`、`mimo-v2.5` 于北京时间 2026-10-21 10:00 下线，建议尽早切换
5. **费用控制**：MiMo 定价请参考官方文档，`ultraspeed` 单价为 `pro` 的 10 倍

## 相关链接

- MiMo 官网: https://mimo.mi.com
- 模型列表: https://mimo.mi.com/static/docs/quick-start/summary/model.md
- API 定价: https://mimo.mi.com/static/docs/price/pay-as-you-go.md
- Zed 配置文档: https://zed.dev/docs/configuring-zed
