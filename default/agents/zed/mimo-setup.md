# Zed Agent MiMo 配置说明

## Provider 划分

Zed 把 MiMo 按计费方式拆成两个互相独立的 `openai_compatible` provider。两者模型 ID 相同，端点与密钥不同，并存且可随时回退，互不覆盖：

- `Xiaomi.MiMo`：按量付费 API，端点 `https://api.xiaomimimo.com/v1`，密钥 `sk-` 前缀；
- `Xiaomi.MiMo.TokenPlan`：Token Plan 订阅套餐，端点 `https://token-plan-cn.xiaomimimo.com/v1`，密钥 `tp-` / `ttp-` 前缀。

`agent.default_model` 当前指向 `Xiaomi.MiMo.TokenPlan` / `mimo-v2.6-flash`。

## 已配置的 MiMo 模型

| provider | 模型 ID | 说明 |
|---|---|---|
| `Xiaomi.MiMo` | `mimo-v2.6-pro` | 专业版，1M 上下文 / 128K 输出，全模态，深度思考 |
| `Xiaomi.MiMo` | `mimo-v2.6-flash` | 快速版，单价更低，适合高频调用 |
| `Xiaomi.MiMo` | `mimo-v2.6-pro-ultraspeed` | 超速版，面向实时交互，单价最高 |
| `Xiaomi.MiMo` | `mimo-v2.5-pro` | 旧版专业版，2026-10-21 下线，仅作过渡 |
| `Xiaomi.MiMo` | `mimo-v2.5` | 旧版全能版，2026-10-21 下线，仅作过渡 |
| `Xiaomi.MiMo.TokenPlan` | `mimo-v2.6-pro` | 同专业版，走套餐额度 |
| `Xiaomi.MiMo.TokenPlan` | `mimo-v2.6-flash` | 同快速版，走套餐额度 |
| `Xiaomi.MiMo.TokenPlan` | `mimo-v2.5-pro` | 旧版专业版，2026-10-21 下线 |
| `Xiaomi.MiMo.TokenPlan` | `mimo-v2.5` | 旧版全能版，2026-10-21 下线 |

三个 2.6 模型的能力位与长度限制相同，仅 `name` / `display_name` 不同。

## API 配置

- 端点（按量付费）：`https://api.xiaomimimo.com/v1`
- 端点（Token Plan 套餐）：`https://token-plan-cn.xiaomimimo.com/v1`
- API 密钥获取：https://platform.xiaomimimo.com

## 使用步骤

### 1. 获取 API 密钥

访问 https://platform.xiaomimimo.com，注册或登录后创建 API 密钥。按量付费密钥为 `sk-` 前缀，Token Plan 套餐密钥为 `tp-` / `ttp-` 前缀，两者不可混用。

### 2. 在 Zed 中使用

1. 打开 Zed 设置，在 `language_models` → `openai_compatible` 下找到对应 provider；
2. 按 provider 分别填入密钥：`Xiaomi.MiMo` 填按量付费密钥，`Xiaomi.MiMo.TokenPlan` 填套餐密钥；
3. 在 Agent 面板的模型选择器中选择 MiMo 模型作为默认模型。

密钥由系统 keychain 保存，不写入 `settings.json`；`settings.json` 只声明 `api_url` 与 `available_models`。

### 3. 模型选择建议

| 场景 | 推荐模型 |
|---|---|
| 复杂项目、长程任务、高价值工作 | `mimo-v2.6-pro` |
| 专业办公场景的高频调用、批量化任务 | `mimo-v2.6-flash` |
| 强调实时交互、对响应速度敏感的生产场景 | `mimo-v2.6-pro-ultraspeed`（仅按量付费） |

## 配置详情

配置文件位置：`~/.config/zed/settings.json`。

两个 provider 并列声明，结构一致，仅 `api_url` 不同：

```json
{
  "language_models": {
    "openai_compatible": {
      "Xiaomi.MiMo": {
        "api_url": "https://api.xiaomimimo.com/v1",
        "available_models": [
          {
            "name": "mimo-v2.6-flash",
            "display_name": "MiMo 2.6 Flash",
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
      },
      "Xiaomi.MiMo.TokenPlan": {
        "api_url": "https://token-plan-cn.xiaomimimo.com/v1",
        "available_models": [
          {
            "name": "mimo-v2.6-flash",
            "display_name": "MiMo 2.6 Flash (Token Plan)",
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

## 注意事项

1. API 密钥安全：不要将 API 密钥提交到版本控制系统；
2. 参数限制：思考模式下 `temperature`、`top_p` 不可自定义，服务端强制为 `1.0` / `0.95`；
3. 思考回传：MiMo 的思考内容走 `reasoning_content` 字段，多轮工具调用若缺少历史 `reasoning_content` 会损失上下文、降低指令遵循度，因此 `capabilities.interleaved_reasoning` 必须为 `true`（Zed 据此把历史思考原样回传）；
4. 旧版下线：`mimo-v2.5-pro`、`mimo-v2.5` 于北京时间 2026-10-21 10:00 下线，建议尽早切换；
5. 费用控制：MiMo 定价请参考官方文档，`ultraspeed` 单价为 `pro` 的 10 倍。

## 相关链接

- MiMo 官网：https://mimo.mi.com
- 模型列表：https://mimo.mi.com/static/docs/quick-start/summary/model.md
- API 定价：https://mimo.mi.com/static/docs/price/pay-as-you-go.md
- Zed 配置文档：https://zed.dev/docs/configuring-zed
