# 资产初始化上下文（asset-init）

从资产初始化实践中提取的**上下文记录**：在量潮知识体系中新建或补全仓库时的场景、流程与注意事项。

## 适用场景

- **领域第二大脑**：新建 `domains/{name}` 领域仓库及配套仓库（app / toolkit / lab / data 记忆仓库）
- **资产聚合容器**：重建或新建 `assets/{name}` 聚合容器（如 profile、journal、intention）
- **已有仓库补全**：仓库已成熟但定义文档缺失（README 为 stub 或缺 LICENSE）

## 命名约定

| 层级 | 规则 | 例子 |
|------|------|------|
| 中文名 | 四字最佳：xx管理（以人为主）/ xx工程（以机为主）/ xx设计 | 密码管理、安全工程、交互设计 |
| 英文名 | 单数，`{name}-management` 或 `{name}-engineering` | `security-engineering` |
| 缩写 | 市场通用缩写；超 8 字母缩写 | `sec`、`ixd`、`entrep` |
| 领域仓库 | `quanttide-{name}` | `quanttide-security` |
| 应用 | `qtcloud-{name}` | `qtcloud-security` |
| 工具集 | `quanttide-{name}-toolkit` | `quanttide-security-toolkit` |
| 实验室 | `quanttide-laboratory-of-{english}` | `quanttide-laboratory-of-security-engineering` |
| 记忆仓库 | `quanttide-{context|journal|intention}-of-{english}` | `quanttide-context-of-security-engineering` |

配套仓库的后缀必须与**英文全名**一致（更名时需同步改名 GitHub 仓库与所有引用）。

## 标准流程

### 1. 调查现状

**必须执行，不可跳过**

- 检查 GitHub 仓库是否已存在（`gh repo view`），存在则复用而非重建
- 检查根仓库是否已注册子模块（`git submodule status`）
- 阅读目标仓库的 README / AGENTS.md / `.gitmodules` / `.quanttide/` 契约

判定类型后选择：新建全套 / 聚合容器 / 补全定义。

### 2. 创建仓库

```bash
gh repo create quanttide/quanttide-<name> --public --add-readme --description "量潮<中文名>"
```

### 3. 注册子模块

```bash
# 根仓库注册领域仓库
git submodule add https://github.com/quanttide/quanttide-<name>.git domains/quanttide-<name>

# 领域仓库内注册配套子模块
cd domains/quanttide-<name>
git submodule add https://github.com/quanttide/qtcloud-<name>.git apps/qtcloud-<name>
git submodule add https://github.com/quanttide/quanttide-<name>-toolkit.git packages/quanttide-<name>-toolkit
git submodule add https://github.com/quanttide/quanttide-laboratory-of-<english>.git examples/default
git submodule add https://github.com/quanttide/quanttide-context-of-<english>.git data/context
git submodule add https://github.com/quanttide/quanttide-journal-of-<english>.git data/journal
git submodule add https://github.com/quanttide/quanttide-intention-of-<english>.git data/intention
```

### 4. 编写文档骨架

**README.md** 结构统一：标题 + 中文名 / 概述 / 领域边界（相邻领域用块引用写明分工）/ 子模块表 / 许可。

**CHANGELOG.md**（Keep a Changelog）：`[Unreleased]` 记子模块注册，`[0.1.0]` 记初始化。

**LICENSE**：复制自同类仓库——领域仓库用 CC BY 4.0；资产聚合容器参照同类（如 intention 用 Apache 2.0）。

### 5. 注册根仓库文档

| 文档 | 更新内容 |
|------|---------|
| `domains/README.md` | 目录结构树新增条目；领域清单表新增行（中文/英文/缩写/描述）；领域项目新增段落 |
| `README.md` | 领域数量 +1；目录结构示例补充 |
| `CHANGELOG.md` | `[Unreleased]` 新增子模块注册条目 |

### 6. 分层提交推送

子模块 → 领域/容器仓库 → 根仓库，逐层提交推送（提交即推送）。

## 注意事项

- **先调查后动手**：避免重复创建仓库（HTTP 422）或破坏已有内容
- **文档与事实一致**：README 子模块表必须与实际 `.gitmodules` 对齐，不存在的子模块不写
- **并行协作安全**：根仓库工作区可能有并行待办，只用 `git add` 具体路径，禁止 `git add -A`
- **远端冲突**：推送被拒时先 `git pull --rebase`，不要强推
- **契约优先**：`.quanttide/agent/contract.yaml` 要求用户确认的操作（git push、删除、改契约）先列清单等确认
- **减法优先**：删除无效内容优先于新增；不确定的内容宁可空着
- **共享仓库双挂载**：同一仓库被多个父仓库挂载（如 qtcrowd 挂 quanttide-crowd 与 quanttide-tech）时，各父仓库需分别更新指针

## 关联

- 循环范式：[loops](../loops/README.md)
- 提交规范：devops-commit
- 子模块操作：devops-submodule
