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

## 插件

### 远程链接

- 源码：https://github.com/liguobao/deepseek-harness-remote
- 官网：dsh.r2049.cn

### 安装

```sh
dsh plugin --profile web add "github:liguobao/deepseek-harness-remote#v0.2.23"
```

> 前提：需先安装 pnpm（插件通过 pnpm 安装）。

### 配置

1. 官网注册登录账户：`https://dsh.r2049.cn`
2. 登录后在网站生成「一次性连接码」（格式如 `XXXX-XXXX`）
3. 打开 Harness Web UI → 设置 → 插件 → 插件配置 → DeepSeek 远程连接
4. 选择「使用连接码」，在「一次性设备授权码」输入框填入连接码
5. 提交后提示「关联成功」，重启 Harness 生效

### 问题

- 不支持选择本地文件夹，只能复制黏贴文件路径。
- 不支持模型切换，建议在本地切换默认配置。
- 不支持权限审批，建议开启 Full Access。
