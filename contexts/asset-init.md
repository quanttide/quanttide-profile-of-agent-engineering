# 资产初始化上下文（asset-init）

从资产初始化实践对话中提取的**活动记录**。内容尽可能忠实保留原始对话中的命令、消息与文档原文——惯例活动在每次初始化中反复复现，照此执行即可。

## 适用场景

- 领域第二大脑：新建 `domains/{name}` 领域仓库及配套仓库
- 资产聚合容器：重建或新建 `assets/{name}` 聚合容器
- 已有仓库补全：仓库成熟但 README 为 stub 或缺 LICENSE

## 命名惯例

对话中反复确认的命名规则：

- 中文名：四字最佳（xx管理 / xx工程 / xx设计）
- 英文名：单数，`{name}-management` 或 `{name}-engineering`
- 缩写：市场通用缩写；超 8 字母缩写（`sec`、`ixd`、`entrep`、`docs`）
- 配套仓库后缀与英文全名一致（更名时需同步改名 GitHub 仓库与所有引用）

## 活动一：调查现状

对话原文：

```bash
# 检查 GitHub 仓库是否已存在（存在则复用，不要重复创建）
for repo in quanttide-design qtcloud-design quanttide-design-toolkit \
  quanttide-laboratory-of-interaction-design \
  quanttide-context-of-interaction-design \
  quanttide-journal-of-interaction-design \
  quanttide-intention-of-interaction-design; do
  echo "== $repo =="
  gh repo view quanttide/$repo --json name 2>&1 | head -2
done

# 检查根仓库是否已注册子模块
git submodule status | grep <name>

# 查看仓库内容与文档
ls <path>/
cat <path>/README.md
cat <path>/.gitmodules
cat <path>/AGENTS.md
```

判定初始化类型：新建全套 / 聚合容器 / 补全定义。

## 活动二：创建仓库

对话原文（以交互设计为例，7 个仓库一条命令链）：

```bash
cd /home/iguo/repos/quanttide && \
gh repo create quanttide/quanttide-design --public --add-readme --description "量潮交互设计领域仓库" 2>&1; \
gh repo create quanttide/qtcloud-design --public --add-readme --description "量潮交互设计云" 2>&1; \
gh repo create quanttide/quanttide-design-toolkit --public --add-readme --description "量潮交互设计工具箱" 2>&1; \
gh repo create quanttide/quanttide-laboratory-of-interaction-design --public --add-readme --description "量潮交互设计实验室" 2>&1; \
gh repo create quanttide/quanttide-context-of-interaction-design --public --add-readme --description "量潮交互设计语境" 2>&1; \
gh repo create quanttide/quanttide-journal-of-interaction-design --public --add-readme --description "量潮交互设计日志" 2>&1; \
gh repo create quanttide/quanttide-intention-of-interaction-design --public --add-readme --description "量潮交互设计意图" 2>&1
```

## 活动三：注册子模块

对话原文：

```bash
# 根仓库注册领域仓库
cd /home/iguo/repos/quanttide && \
git submodule add https://github.com/quanttide/quanttide-design.git domains/quanttide-design 2>&1 && \
cd domains/quanttide-design && \
git submodule add https://github.com/quanttide/qtcloud-design.git apps/qtcloud-design 2>&1 && \
git submodule add https://github.com/quanttide/quanttide-design-toolkit.git packages/quanttide-design-toolkit 2>&1 && \
git submodule add https://github.com/quanttide/quanttide-laboratory-of-interaction-design.git examples/default 2>&1 && \
git submodule add https://github.com/quanttide/quanttide-context-of-interaction-design.git data/context 2>&1 && \
git submodule add https://github.com/quanttide/quanttide-journal-of-interaction-design.git data/journal 2>&1 && \
git submodule add https://github.com/quanttide/quanttide-intention-of-interaction-design.git data/intention 2>&1
```

## 活动四：编写领域仓库文档

### README.md 原文模板

```markdown
# quanttide-design

量潮交互设计

## 概述

量潮交互设计（quanttide-design）是量潮知识管理体系中的**交互设计**领域，以工程化方式承载产品界面布局与交互流程的设计实践。

## 领域边界

- **界面布局**：页面结构、信息层级、导航与组件摆放
- **交互流程**：用户完成关键任务的操作路径、状态流转与反馈
- **设计原则**：一致性、反馈即时、极简主义等设计指导思想
- **设计工程化**：设计文档标准化、设计稿与代码衔接、设计审查

> 与 product 领域的分工：本领域承载「用户怎么用」（界面与交互），product 承载「做什么和为什么」（需求与方案）。
> 与 asset 领域的分工：本领域承载「交互设计方法」，asset 承载「设计资产的组织与浏览」。

## 子模块

| 路径 | 说明 |
|------|------|
| `apps/qtcloud-design` | QtCloud 交互设计云 (git submodule) |
| `packages/quanttide-design-toolkit` | 交互设计工具集 (git submodule) |
| `examples/default` | 交互设计实验室 (git submodule → quanttide-laboratory-of-interaction-design) |
| `data/context` | 交互设计语境 (git submodule → quanttide-context-of-interaction-design) |
| `data/journal` | 交互设计日志 (git submodule → quanttide-journal-of-interaction-design) |
| `data/intention` | 交互设计意图 (git submodule → quanttide-intention-of-interaction-design) |

## 许可

[CC BY 4.0](LICENSE)
```

### CHANGELOG.md 原文模板

```markdown
## [Unreleased]

### 新增

- 注册子模块：`apps/qtcloud-design`、`packages/quanttide-design-toolkit`、`examples/default`
- 注册子模块：`data/context`、`data/journal`、`data/intention`

## [0.1.0] - 2026-08-16

### 新增

- 初始化交互设计领域仓库
```

### LICENSE

```bash
cp /home/iguo/repos/quanttide/domains/quanttide-security/LICENSE /home/iguo/repos/quanttide/domains/quanttide-<name>/LICENSE
```

领域仓库用 CC BY 4.0；资产聚合容器参照同类（如 intention 用 Apache 2.0）。

## 活动五：领域仓库提交推送

对话原文（提交即推送）：

```bash
cd /home/iguo/repos/quanttide/domains/quanttide-design && \
git add -A && git status --short && \
git commit -m "chore: 初始化交互设计领域仓库（注册配套子模块）" 2>&1 && \
git push 2>&1
```

## 活动六：注册根仓库文档

对话中每次反复执行的三文档同步：

### domains/README.md — 三处更新

```bash
# 1. 目录结构树（按字母序插入）
# ├── quanttide-design/      # 交互设计

# 2. 领域清单表新增行（放在对应分组）
# | 交互设计 | interaction-design | `ixd` | 产品界面布局与交互流程的设计工程化实践。 |

# 3. 领域项目新增段落
# ### quanttide-design
# 量潮交互设计，专注于产品界面布局与交互流程的设计工程化实践。
# **功能：**
# - 界面布局（页面结构、信息层级、导航与组件摆放）
# - 交互流程（操作路径、状态流转与反馈设计）
# - 设计原则（一致性、反馈即时、极简主义）
# - 设计工程化（设计文档标准化、设计稿与代码衔接）
```

### README.md

```bash
# 领域数量 +1，目录结构示例补充
# ├── domains/  # 领域轴：31 个领域仓库
# │   ├── quanttide-design/        # 交互设计
```

### CHANGELOG.md

```markdown
- 新增 `domains/quanttide-design` 子模块：交互设计（CC BY 4.0 许可证）
   - 注册子模块：`apps/qtcloud-design`、`packages/quanttide-design-toolkit`、`examples/default`
   - 注册子模块：`data/context`、`data/journal`、`data/intention`
```

## 活动七：根仓库提交推送

对话原文：

```bash
cd /home/iguo/repos/quanttide && \
git add domains/quanttide-design domains/README.md README.md CHANGELOG.md && \
git status --short && \
git commit -m "feat: 新增交互设计领域（quanttide-design）" 2>&1 && \
git push 2>&1
```

注意：根仓库工作区可能有并行待办，只用 `git add` 具体路径，禁止 `git add -A` 全量提交。

## 活动八：验证

对话原文：

```bash
cd /home/iguo/repos/quanttide && \
git submodule status domains/quanttide-design && \
cd domains/quanttide-design && \
git log --oneline -2 && \
git submodule status | head -7
```

## 惯例活动：已有仓库补全

适用于仓库成熟但 README 是 stub 的场景（如 quanttide-asset、quanttide-media）：

- 重写 README：概述 / 领域边界 / 子模块表（**必须与实际 `.gitmodules` 对齐，不存在的子模块不写**）/ 许可
- 若无 LICENSE：`cp` 同类仓库 LICENSE
- CHANGELOG 追加：

```markdown
## [Unreleased]

### Changed
- 重写 README：补全领域定义（概述、领域边界、子模块结构、许可 CC BY 4.0）
```

- 提交消息：`docs: 初始化领域定义（重写 README + LICENSE）`

## 惯例活动：英文更名

对话原文（documentation-engineering → document-engineering）：

```bash
# 1. GitHub 仓库改名（4 个配套仓库，旧 URL 自动重定向）
gh repo rename quanttide-laboratory-of-document-engineering \
  --repo quanttide/quanttide-laboratory-of-documentation-engineering --yes 2>&1

# 2. 领域仓库 .gitmodules URL 更新 + 同步
cd /home/iguo/repos/quanttide/domains/quanttide-docs && \
sed -i 's/of-documentation-engineering/of-document-engineering/g' .gitmodules && \
git submodule sync 2>&1

# 3. 更新 README 引用与根仓库领域清单
# 4. 子模块 README 标题同步（自动生成的初始 README 标题为旧仓库名）
for sm in examples/default data/context data/journal data/intention; do
  old=$(head -1 $sm/README.md)
  new=$(echo "$old" | sed 's/of-documentation-engineering/of-document-engineering/')
  echo "$new" > $sm/README.md
  (cd $sm && git add README.md && git commit -m "docs: README 标题同步仓库更名（document-engineering）" -q && git push -q)
done

# 5. 分层提交：子模块 → 领域仓库（.gitmodules+README）→ 根仓库（领域清单+指针）
```

## 惯例活动：挂载已有产品仓库

适用于已有产品应用仓库（qtcrowd、qtdocs）挂入领域 `apps/`：

```bash
cd /home/iguo/repos/quanttide/domains/quanttide-crowd && \
git submodule add https://github.com/quanttide/qtcrowd.git apps/qtcrowd 2>&1
```

- README 子模块表新增行：`| `apps/qtcrowd` | 量潮众包平台 (git submodule → qtcrowd，与 quanttide-tech/apps 共用) |`
- CHANGELOG：`- 注册子模块：`apps/qtcrowd`（量潮众包平台，与 quanttide-tech/apps 共用）`
- 领域仓库提交：`chore: 注册 apps/qtcrowd 子模块（量潮众包平台）`
- 根仓库提交：`chore: 更新 quanttide-crowd 子模块指针（注册 apps/qtcrowd）`
- **共享仓库双挂载**：同一仓库被多个父仓库挂载时（如 qtcrowd 挂 quanttide-crowd 与 quanttide-tech），各父仓库是独立克隆，需分别更新指针

## 注意事项（对话中反复出现的教训）

- **先调查后动手**：避免重复创建仓库（HTTP 422）或破坏已有内容
- **远端冲突**：推送被拒时先 `git pull --rebase`，不要强推（对话中 rebase 合并过 26 个并行提交）
- **契约优先**：`.quanttide/agent/contract.yaml` 要求用户确认的操作（git push、删除、改契约）先列清单等确认
- **减法优先**：删除无效内容优先于新增；不确定的内容宁可空着
- **文档与事实一致**：README 子模块表与实际 `.gitmodules` 对齐（对话中曾误写不存在的 `data/context` 后修正）

## 关联

- 循环范式：[loops](../loops/README.md)
- 提交规范：devops-commit
- 子模块操作：devops-submodule
