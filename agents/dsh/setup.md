# 安装和配置

建议使用其他智能体安装和配置 dsh。

## 官网

- 源码：https://github.com/deepseek-ai/deepseek-harness

### 安装

**环境要求**

- Node.js：`^22.19.0` 或 `>=24.0.0`
- pnpm：`11.7.0`（插件安装依赖 pnpm）

**安装方式（二选一）**

方式一：全局安装（推荐，命令可用）

```sh
npm install -g @deepseek-ai/dsh
```

方式二：从源码构建

```sh
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

### 配置

启动 Web 界面：

```sh
dsh web --port 3080
```

访问地址 `127.0.0.1:3080`

设置开机自启动，以方便直接在本地访问。

### 模型配置

dsh 是 agent 框架，本身不内置模型，需配置模型提供方。

**DeepSeek 官方（内置提供方）**

DeepSeek 是内置提供方，无需手动定义 provider，只需：

1. 配置 `DEEPSEEK_API_KEY` 环境变量（或写入 `.dsh/.credentials.yaml`）
2. 默认模型设为 `deepseek-official / deepseek-v4-flash`

`settings.yaml` 关键片段：

```yaml
agent-default-model:
  provider: deepseek-official
  model: deepseek-v4-flash
```

> 注意：模型变更在下一次请求时生效，无需重启。
