# Zed Agent StepFun 配置说明

## 已配置的 StepFun 模型

在 Zed 的 `settings.json` 中已添加 StepFun（阶跃星辰）模型，provider 为 `StepFun`：

| 模型 | 说明 | 特点 |
|------|------|------|
| **step-5-preview** | 旗舰预览版（2026-09-16 发布） | 1M 上下文 / 1M 输出，文图视频输入，深度思考（low/medium/high） |
| **step-3.7-flash** | 高效多模态 MoE（196B/激活约 11B） | 256K 上下文 / 256K 输出，文图视频输入，深度思考（low/medium/high） |
| **step-3.5-flash** | 快速版 | 256K 上下文 / 256K 输出，纯文本输入，深度思考（low/high） |

## API 配置

- **API 端点（中国站）**: `https://api.stepfun.com/v1`
- **API 端点（国际站）**: `https://api.stepfun.ai/v1`
- **API 密钥获取**: https://platform.stepfun.com

## 使用步骤

### 1. 获取 API 密钥

1. 访问 https://platform.stepfun.com
2. 注册/登录账号
3. 创建 API 密钥

### 2. 在 Zed 中使用

1. 打开 Zed 编辑器
2. 打开设置（Settings），在 `language_models` → `openai_compatible` → `StepFun` 下填写 API 密钥
3. 在 Agent 面板的模型选择器中选择 StepFun 模型

### 3. 模型选择建议

| 场景 | 推荐模型 |
|------|---------|
| 复杂项目、长程任务、多模态理解 | **step-5-preview** |
| 高性价比的日常编码与多模态任务 | **step-3.7-flash** |
| 纯文本、高频轻量调用 | **step-3.5-flash** |

## 配置详情

配置文件位置：
```
~/.config/zed/settings.json
```

能力位（capabilities）按 StepFun Chat Completions 特性填写：工具调用开启、并行工具调用关闭、思考内容（`reasoning_content`）交错输出（`interleaved_reasoning: true`）、使用 `max_tokens` 参数。思考档位用 `reasoning_effort: "high"`。

> 注意：`step-5-preview` 目录先在国际站（api.stepfun.ai）上架；若中国站报 `model not found`，把 `api_url` 换成国际站端点或暂时移除该条目。
