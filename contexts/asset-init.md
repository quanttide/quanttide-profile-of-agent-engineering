# 资产初始化上下文（asset-init）

从资产初始化实践对话中提取的**活动记录**。先忠实记录原始对话中的活动（命令、消息、文档原文），再总结其中反复出现的惯例与教训。本文档覆盖「领域第二大脑」创建、补全、更名、挂载等全部实践形态，并整理背后的体系背景、对话全貌、格式契约与关键决策，供后续同类工作复用。

## 背景与体系

### 体系是什么

「量潮第二大脑（quanttide）」是一套基于 **Git 子模块多仓架构**的知识管理体系，核心设计思想：

| 原则 | 含义 |
|------|------|
| **正交分解** | 能力轴（How it runs，`assets/`）、领域轴（What it expresses，`domains/`）、主体轴（Who it is，`default/` 法人主体档案）三轴分离 |
| **单一事实源** | 子模块独立演进，父仓库只追踪引用 |
| **知识即代码** | 文档、标准、工具、示例统一纳入版本控制 |
| **统一规范**（本次对话新增元原则） | 三轴正交解决「怎么分」，统一规范解决「怎么统一」——统一结构 / 信息集中 / 关联分析 |

### 本次对话做了什么

本次会话围绕「创建领域第二大脑」展开，先后完成：

- **领域第二大脑创建**：密码管理（secret）、安全工程（security）、健康管理（health）、交互设计（design）、创业管理（entrep）、联盟管理（alliance）、众包管理（crowd）、文档工程（docs）等新领域，以及 media、asset、profile 等既有仓库的初始化/补全；
- **配套仓库体系**：每个领域按统一模式配齐「应用云 + 工具集 + 实验室 + data 三件套（语境/日志/意图）」；
- **统一规范元原则落地**：将「统一规范」写入根 README、ROADMAP、AGENTS，并以安全工程领域为试点编写 `data/intention` 产品意图范例；
- **资产体系初始化**：补全 quanttide-asset 领域定义，并参照 qtfounder studio 的资产页面模式规划 qtcloud-asset 的 studio（写入 ROADMAP）；
- **版本与协作**：主仓库发布 patch 版本、批量提交子模块指针、把产品应用（qtcrowd、qtdocs）挂入领域 `apps/`、初始化官网前台脚手架等。

一句话概括：**每个「领域第二大脑」就是该领域信息的唯一集中点**——用同一套结构（统一框架）收纳该领域全部信息（日志、意图、语境、档案、文档、应用数据），经统一命名与契约登记建立跨领域关联，支撑关联分析。

## 活动记录

以下以交互设计（quanttide-design）为例忠实记录主流程命令；完整 37 回合及各个领域的实践见「对话流程总览」。

### 活动一：调查现状

**必须执行，不可跳过。** 对话原文：

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

### 活动二：创建仓库

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

### 活动三：注册子模块

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

### 活动四：编写领域仓库文档

#### README.md 原文模板

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

#### CHANGELOG.md 原文模板

```markdown
## [Unreleased]

### 新增

- 注册子模块：`apps/qtcloud-design`、`packages/quanttide-design-toolkit`、`examples/default`
- 注册子模块：`data/context`、`data/journal`、`data/intention`

## [0.1.0] - 2026-08-16

### 新增

- 初始化交互设计领域仓库
```

#### LICENSE

```bash
cp /home/iguo/repos/quanttide/domains/quanttide-security/LICENSE /home/iguo/repos/quanttide/domains/quanttide-<name>/LICENSE
```

### 活动五：领域仓库提交推送

对话原文（提交即推送）：

```bash
cd /home/iguo/repos/quanttide/domains/quanttide-design && \
git add -A && git status --short && \
git commit -m "chore: 初始化交互设计领域仓库（注册配套子模块）" 2>&1 && \
git push 2>&1
```

### 活动六：注册根仓库文档

对话中每次反复执行的三文档同步：

#### domains/README.md — 三处更新

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

#### README.md

```bash
# 领域数量 +1，目录结构示例补充
# ├── domains/  # 领域轴：31 个领域仓库
# │   ├── quanttide-design/        # 交互设计
```

#### CHANGELOG.md

```markdown
- 新增 `domains/quanttide-design` 子模块：交互设计（CC BY 4.0 许可证）
   - 注册子模块：`apps/qtcloud-design`、`packages/quanttide-design-toolkit`、`examples/default`
   - 注册子模块：`data/context`、`data/journal`、`data/intention`
```

### 活动七：根仓库提交推送

对话原文：

```bash
cd /home/iguo/repos/quanttide && \
git add domains/quanttide-design domains/README.md README.md CHANGELOG.md && \
git status --short && \
git commit -m "feat: 新增交互设计领域（quanttide-design）" 2>&1 && \
git push 2>&1
```

### 活动八：验证

对话原文：

```bash
cd /home/iguo/repos/quanttide && \
git submodule status domains/quanttide-design && \
cd domains/quanttide-design && \
git log --oneline -2 && \
git submodule status | head -7
```

### 变体活动记录

#### 资产聚合容器（quanttide-profile 重建）

注册系列档案仓库的对话原文：

```bash
cd /home/iguo/repos/quanttide/assets/quanttide-profile && \
git submodule add https://github.com/quanttide/quanttide-profile-of-business-entity.git default/company 2>&1 && \
for pair in "agent:quanttide-profile-of-agent-engineering" "course:quanttide-profile-of-course-development" "customer:quanttide-profile-of-customer-relations" "data:quanttide-profile-of-data-engineering" "delib:quanttide-profile-of-deliberation-management" "econ:quanttide-profile-of-economic-modeling" "execute:quanttide-profile-of-execution-management" "health:quanttide-profile-of-health-management" "human:quanttide-profile-of-human-resources" "innov:quanttide-profile-of-innovation-management" "product:quanttide-profile-of-product-development"; do \
  path="${pair%%:*}"; repo="${pair##*:}"; \
  git submodule add "https://github.com/quanttide/$repo.git" "domains/$path" 2>&1; \
done
```

容器文档（README）以「仓库定位 / 仓库结构 / 子模块管理 / 关联」组织，随后走活动五至八。

#### 已有仓库补全（quanttide-asset、quanttide-media）

仓库成熟但 README 是 stub 的场景。对话原文：

```bash
# 重写 README：概述 / 领域边界 / 子模块表 / 许可
# 若无 LICENSE：cp 同类仓库 LICENSE
# CHANGELOG 追加：
# ## [Unreleased]
# ### Changed
# - 重写 README：补全领域定义（概述、领域边界、子模块结构、许可 CC BY 4.0）
```

提交消息：`docs: 初始化领域定义（重写 README + LICENSE）`

#### 挂载已有产品仓库（qtcrowd、qtdocs）

对话原文：

```bash
cd /home/iguo/repos/quanttide/domains/quanttide-crowd && \
git submodule add https://github.com/quanttide/qtcrowd.git apps/qtcrowd 2>&1
```

- README 子模块表新增行：`| `apps/qtcrowd` | 量潮众包平台 (git submodule → qtcrowd，与 quanttide-tech/apps 共用) |`
- CHANGELOG：`- 注册子模块：`apps/qtcrowd`（量潮众包平台，与 quanttide-tech/apps 共用）`
- 领域仓库提交：`chore: 注册 apps/qtcrowd 子模块（量潮众包平台）`
- 根仓库提交：`chore: 更新 quanttide-crowd 子模块指针（注册 apps/qtcrowd）`

#### 英文更名（documentation-engineering → document-engineering）

对话原文：

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

## 对话流程总览

### 全对话时序（37 回合）

以下按回合列出驱动对话的用户指令与对应结果（已去敏，仅保留实质内容；文中 `secret` 指「密码管理」领域/仓库名称，并非任何密钥）：

| 回合 | 用户指令（实质内容） | 关键动作与结果 |
|------|---------------------|----------------|
| 1 | 创建领域第二大脑 quanttide-secret | 确认中文名「密码管理」（凭证/密钥管理）；创建领域仓库骨架（README/许可/CHANGELOG），注册为主仓库子模块，登记到领域清单 |
| 2 | 创建 qtcloud-secret 关联 apps/、quanttide-secret-toolkit 关联 packages/、quanttide-laboratory-of-secret-management 关联 examples/ | 首次确立「应用 + 工具集 + 实验室」三配套仓库模式（实验室用 `-of-secret-management` 后缀） |
| 3 | 类似创建 quanttide-security 量潮网络安全 | 按同一流程创建安全领域仓库骨架 |
| 4–5 | yes；量潮安全云；量潮网络安全工具箱；software-security 量潮网络安全实验室 | 为 security 创建三个配套仓库；实验室先按 `-of-software-security` 命名 |
| 6 | software-security vs security-engineering? | 对比两个英文命名；最终确定 **security-engineering（安全工程）** 更合适（语义对齐、命名规则对齐、边界自洽），执行仓库更名 |
| 7 | 网络安全 -> 安全工程 | 领域中文名由「网络安全」改为「安全工程」，全链路（领域仓库、子模块、GitHub 描述、根仓库文档）同步 |
| 8 | 如何定义这个领域呢 | 形成领域定义草案模板：概述（一句话定位）→ 领域边界（能力域表）→ 与相邻领域的分工 → 子模块现状与规划；落盘到领域 README |
| 9 | 提交所有更新 | 批量提交/推送全部子模块指针，主仓库工作区恢复干净 |
| 10 | 创建 data/context 和 journal 仓库 | 为 security 创建语境、日志仓库（`quanttide-context-of-security-engineering` 等），确立 data 仓库命名模式 |
| 11 | 主仓库发布新的 patch | 按发布流程发布主仓库 patch 版本：预检查 → 固化 Unreleased → 记录发布日志 → 打标签 → 发布 |
| 12 | （语音转写思考）统一规范核心思想；记录到 quanttide-tech 的 journal 子仓库 qtcloud 日志，记录前先 pull | 整理语音为结构化日志：**统一规范 → 系统一致性**；产品信息集中 → 统一框架解读 → 关联分析；对话语言、编程语言（测试-文档-代码三位一体）、数据语言、所有云皆同一套路 |
| 13 | 根据我提出来的思路，各个领域第二大脑的产品思路应当如何更新？如何落实到具体文档？ | 提出三原则（P1 统一规范 / P2 信息集中 / P3 关联分析）与三层文档落实清单；用户先后否掉两个方向（「不是我想要的」「和我现在的设计思路对比」）后收敛 |
| 14 | 看不懂，再通俗一些解释 | 改用大白话复述：所有东西按同一套规矩、信息都集中、集中后可互相串起来分析；先立规矩（3 份总文档）再写说明书（每领域一份，先写安全工程） |
| 15 | yes | 落地根 README + ROADMAP + AGENTS 三份元文档；新建安全工程意图仓库 `data/intention`，写入范例（背景动机 → 统一框架 → 模块设计 → 建设路径） |
| 16–20 | 初始化 quanttide-health 领域仓库和对应的实验室、平台和工具库。health-management 健康管理；这个云比较特殊，要特别注意数据安全。个人相对比较全面，家庭主要是大病的管理，企业主要是共同问题的管理；创建 data/context 和 journal 仓库；yes | 创建健康管理领域（qtcloud-health 已存在则复用）；领域边界按对象维度重写（个人全面 / 家庭大病 / 企业共同问题 / 健康数据安全底线）；补齐 context/journal/intention，与 security 结构完全对齐 |
| 21–22 | 初始化 quanttide-asset，并根据 qtfounder studio 的 asset 页面规划 qtcloud-asset 的 studio，写到对应的 ROADMAP；为什么修改 CHANGELOG | 补全 quanttide-asset 领域定义（README）；参照「资产契约 + 目录引擎 + 通用页面（结构即界面、只读浏览）」模式将 Studio 规划写入 qtcloud-asset ROADMAP；澄清 CHANGELOG 维护规范并采用最小干预方案 |
| 23 | 创建领域仓库 quanttide-design，交互设计 Interaction Design | 全套创建交互设计领域（7 个仓库），缩写采用既有约定 `ixd` |
| 24 | 初始化 quanttide-profile | 将已被清空的「量潮工作档案」聚合容器按同类容器（roadmap/intention）模式重建，聚合 12 个 `profile-of-*` 系列档案仓库 |
| 25 | 根据 quanttide-tech 新增的 qtcrowd 相关资料，更新 quanttide-product 的 profile | 在 product 档案仓库新增 `qtcrowd/` 条目（产品档案 index + 需求档案 requirement） |
| 26–27 | 根据我们的活动总结资产初始化的经验，写成 skill asset-init；写的不太好，删除 | 将资产初始化经验写成技能；用户不满意后删除并完整回滚 |
| 28 | 创建领域第二大脑 quanttide-entrep | 按命名规则默认「创业管理 / entrepreneurship-management / entrep」，全套创建 |
| 29 | 创建领域第二大脑量潮联盟管理 quanttide-alliance | 创建「联盟管理 / alliance-management / alliance」，放「沟通与管理」组 |
| 30 | 创建 quanttide-crowd 第二大脑 | 把众包从产品应用提升为独立领域：「众包管理 / crowdsourcing-management / crowd」 |
| 31 | qtcrowd 加入到 apps/ | 将既有产品应用 qtcrowd 挂入众包领域 `apps/`（参照 health 挂 qthealth 先例），README 子模块表保持文档同步 |
| 32 | qtcrowd 初始化 src/site | 参照既有惯例（Vite + React 官网前台）初始化官网脚手架，三页（首页/发单/接单），构建与 lint 验证通过，跨两个父仓库分层推送 |
| 33 | yes | 收尾两个遗留事项：asset 初始化补 CHANGELOG 记录；design 指针跟进（用户已并行处理） |
| 34 | 初始化 quanttide-media | 成熟仓库（11 个子模块齐全）但 README 仅 1 行 stub：补全领域定义 + 补许可；对齐目录注释「新媒体运营 / social-media / media」 |
| 35 | 创建领域第二大脑 quanttide-docs 量潮文档工程 | 复用已有 toolkit，新建其余 6 仓：「文档工程 / documentation-engineering / docs」 |
| 36 | Document Engineering 似乎更常用？ | 采纳更标准的单数 `document-engineering`，4 个配套仓库更名并全链路同步 |
| 37 | yes | 将 qtdocs（量潮文档中心）挂入文档工程领域 `apps/` |

### 标准领域创建流程（7 步）

从对话中提炼的「全新领域第二大脑」标准流程（与上文「活动一至八」基本一一对应，前者为抽象步骤，后者为具体命令；第 6 步合并了活动六、七）：

1. **先调查后动手**：检查 GitHub 上是否已有同名仓库（避免重复创建报错）；查看最近创建领域的仓库结构作为模板；确认领域中文名、英文名、缩写（不确定时向用户确认，用户不回应则按命名规则取默认值）。
2. **创建 GitHub 仓库**（全部公开）：领域仓库 + 应用云 + 工具集 + 实验室 + data 三件套（语境/日志/意图），共 7 个，均带 README 初始提交。
3. **注册子模块**：`git submodule add`，领域仓库内部路径约定：`apps/qtcloud-{name}`、`packages/{name}-toolkit`、`examples/default`（指向实验室）、`data/{context,journal,intention}`。
4. **编写领域仓库骨架**：README（概述 + 领域边界 + 与相邻领域的分工 + 子模块表 + 许可）、LICENSE、CHANGELOG（`[0.1.0]` 初始化记录）。遵循「减法优先」——只放骨架，不预建空目录或虚构子模块。
5. **分层提交推送**（提交即推送）：先提交推送子模块仓库 → 再提交推送领域仓库（含指针与 README/CHANGELOG 更新）→ 最后提交推送主仓库。
6. **根仓库注册**：`domains/README.md` 三处（目录结构块 + 领域清单行 + 领域项目小节）、根 `README.md`（领域数量 +1）、根 `CHANGELOG.md`（Unreleased 新增条目）。
7. **验证**：子模块指针与各 HEAD 一一对应、主仓库与远端同步、无残留未提交项。

### 其他可复用流程模式

除主流程外，对话还沉淀了以下可复用模式（更名 / 已有仓库补全 / 聚合容器 / 产品应用挂载已在「变体活动记录」中给出具体命令，此处不重复）：

- **配套三仓追加**（回合 2/5）：为已建领域补 `apps/`、`packages/`、`examples/default` 三个仓库并注册。
- **data 三件套追加**（回合 10/19）：补 `data/context`、`data/journal`，再按需补 `data/intention`。
- **意图仓库**（回合 15/20）：意图主文档 `index.md` 标准结构 = 背景与动机 → 统一框架（三原则落实）→ 云模块设计 → 建设路径；写作素材取自该领域 journal 日志与用户产品思路。
- **更名流程**（回合 6/7/36）：GitHub 仓库改名（旧 URL 自动重定向）→ 领域仓库 `.gitmodules` URL 更新 + `git submodule sync` + README 引用更新 → 各子模块 README 标题同步 → 根仓库领域清单/描述同步 → 逐层提交推送 → 全库检索旧名清零验证。具体命令见「变体活动记录 · 英文更名」。
- **已有仓库补全**（回合 21/24/34，quanttide-asset / profile / media 模式）：先调查现状（是否成熟、README 是否 stub、缺什么），再按类型处理：补全领域定义（asset/media）、重建聚合容器（profile）。具体命令见「变体活动记录 · 已有仓库补全」。
- **聚合容器初始化**（回合 24）：能力轴容器仓库（档案/日志/意图/路线图）参照同类容器组织，注册既有 `-of-{name}` 系列仓库，许可证参照同类容器（容器用 Apache 2.0，领域仓库用 CC BY 4.0）。具体命令见「变体活动记录 · 资产聚合容器」。
- **产品应用挂载**（回合 31/37）：既有产品应用（qtcrowd、qtdocs）与领域配套云（qtcloud-crowd、qtcloud-docs）是两个层级；挂载进领域 `apps/` 时保持 README 子模块表与 CHANGELOG 同步。具体命令见「变体活动记录 · 挂载已有产品仓库」。
- **官网前台初始化**（回合 32）：`src/site` 惯例 = Vite + React + TypeScript 官网，页面内容源自该产品意图档案；构建与 lint 验证通过后再提交。
- **发布流程**（回合 11）：预检查（版本号格式、CHANGELOG 匹配、Notes 提取、标签不存在、工作区干净、子模块同步）→ 固化 Unreleased → 记录发布日志 → 打标签 → 发布。

### 操作检查清单

- [ ] 动手前先 `gh repo view` 检查仓库是否已存在（避免重复创建）；
- [ ] 不确定领域中文名/英文名/缩写时先向用户确认，用户不回应则按命名规则取默认并注明可调整；
- [ ] 只 `git add` 具体路径，禁止 `git add -A`；推送被拒先 `git pull --rebase`；
- [ ] 按「子模块 → 领域仓库 → 主仓库」分层提交，提交即推送；
- [ ] 领域 README 遵循「概述 → 领域边界 → 相邻领域分工 → 子模块表 → 许可」结构；
- [ ] 所有用户可见变更同步更新 CHANGELOG；规划类内容（如 ROADMAP）不记 CHANGELOG；
- [ ] 文档遵循格式规范：最多 3 级标题、代码块带语言、中文引号「」、文件名小写；
- [ ] 完成后验证：指针一致、工作区干净、与远端同步。

> **交付形态教训**（回合 26–27）：对话中「写 asset-init 技能 → 用户不满意 → 删除回滚」表明交付物形态需贴近用户期望（更偏操作清单而非流程描述），建议先做最小可用版本再迭代。

### 可复用能力清单

本上下文沉淀的实践可直接复用为自动化能力：

1. **流程引擎**：标准创建流程（7 步）与各变体流程可编排为可执行步骤；
2. **格式校验**：按文档工程契约（标题层级、代码块语言、命名规范）校验产出文档；
3. **契约生成**：按数字资产契约字段（title/type/category/audience/path/description）生成资产登记，并支持 `structure:` / `relations:` 关联声明；
4. **命名助手**：按命名规则与仓库命名模式自动生成全套仓库名；
5. **审核规则**：按 AI 执行审核契约区分需确认与无需确认的操作，执行前列清单、等确认；
6. **统一规范检查**：对照统一结构与三原则检查领域仓库是否达标（信息集中、关联可分析）。

## 格式规范与契约

### 文档工程契约（`.quanttide/docs/contract.yaml`）

对话中读取到的契约原文（即文档格式规范本身）：

```yaml
# 量潮第二大脑 — 文档工程契约
# 模块定位：知识管理文档规范

standards:
  format:
    syntax: markdown
    markdown_flavor: gfm

  headings:
    max_level: 3          # 标题最多 3 级
    document_title: h1    # 文档标题用 h1
    section: h2           # 章节用 h2
    subsection: h3        # 小节用 h3

  code_blocks:
    language_required: true   # 代码块必须标注语言
    fence_style: fenced       # 使用围栏式代码块

  lists:
    unordered: "-"
    ordered: "1."

  links:
    reference: "[text](url)"
    inline: "[text](url)"

naming:
  filename:
    case: lowercase        # 文件名小写
    separators: ["_", "-"] # 分隔符用下划线或连字符
    example: my-document-name.md

  directory:
    case: lowercase
    separators: ["_", "-"]
    plural: true           # 目录名用复数
    example: my_directory/
```

配套的「文档格式技能」补充规则：最多 3 级标题、尽量少用表格与加粗、中文引号使用「」、代码块必须带语言标识（围栏式）。

### 数字资产契约（`.quanttide/asset/contract.yaml`）

契约按**双轴**组织（能力轴 + 领域轴），与 `.gitmodules` 对齐，每个资产条目包含固定字段。示例：

```yaml
# 量潮第二大脑 — 数字资产契约
# 模块定位：知识管理多仓架构
# 分类依据：能力轴 + 领域轴

assets:   # 能力轴（How it runs）
  quanttide_profile:
    title: 量潮工作档案
    type: docs
    category: asset
    audience: human
    path: assets/quanttide-profile
    description: 量潮工作档案

domains:  # 领域轴（What it expresses）
  quanttide_data:
    title: 量潮数据工程
    type: app
    category: domain
    audience: engine
    path: domains/quanttide-data
    description: 量潮数据工程领域
```

**条目字段**：`title`（标题）、`type`（docs / app 等）、`category`（asset / domain / default 等）、`audience`（human / ai / engine）、`path`（仓库内相对路径）、`description`（一句话描述）。

**演进方向**（本次对话的规划）：契约从「静态登记」走向「可分析」——为条目补充 `structure:`（统一结构声明）与 `relations:`（相邻领域分工/关联声明），使统一框架机器可读；资产云侧配套「契约解析器 → 扫描资产目录 → 生成资产清单」的能力。

### AI 执行审核契约（`.quanttide/agent/contract.yaml`）

适用于带契约限制的仓库（如 qtcloud-asset），强制约束 AI 执行行为：

| 维度 | 规则要点 |
|------|---------|
| **触发条件** | 每次对话开始时、每次执行操作前、用户提到 删除/修改/推送/部署/执行/提交/清理 等关键词时，必须读取本契约 |
| **需审核的操作** | 删除/批量重命名/清空文件；git push、删分支、force push、reset --hard、rebase -i；修改远程设置；执行外部脚本、安装依赖、修改敏感配置与凭据；删除容器/数据库记录；修改 CI/CD 与权限配置；修改 `.quanttide/`、`.agents/`、AGENTS.md；破坏性命令 |
| **无需审核的操作** | 读取类操作；创建/修改普通文件、写文档、写测试；运行测试/lint/格式化/构建（不涉及部署）；git add、commit、checkout、branch、pull、非 force merge；创建容器、启动开发服务器 |
| **执行规范** | ① 自动读取契约；② 执行前列出操作清单并标注风险等级；③ 需审核操作等待用户明确回复「可以执行/同意」后才执行；④ 完成后简要反馈结果 |

### 仓库与提交规范

- **CHANGELOG**：遵循 Keep a Changelog 格式；新领域写完整 `## [0.1.0] - 日期` 初始化记录；常规变更记入 `[Unreleased]` 段；「对用户可见的变更须同步更新 CHANGELOG」，但 ROADMAP 等规划类内容按惯例不记（最小干预原则）。
- **许可证**：领域仓库一律 **CC BY 4.0**；资产/能力轴容器仓库参照同类容器（如 intention、platform）用 **Apache 2.0**；既有成熟应用（如健康云）保留其原有许可证（Apache 2.0）。
- **提交信息**：领域与主仓库用 Conventional Commits 风格（中文描述），如 `feat: init quanttide-xxx domain`、`chore: 同步子模块指针`；日志仓库按惯例用日期作提交信息。
- **分层提交 / 提交即推送**：子模块 → 领域仓库 → 主仓库逐层提交推送，禁止越级；子模块内的文件必须在子模块仓库内提交推送，父仓库只更新指针引用（详见「总结 · 分层提交模式」）。
- **并行协作安全**：只用 `git add` 具体路径、**禁止 `git add -A`**（避免卷入用户并行修改）；远端推送被拒先 `git pull --rebase`；不触碰用户工作区中并行待提交项；子模块处于 detached HEAD 时先 `git checkout main` 再拉取。
- **读写纪律**：每个新回合编辑文件前必须先 read；fresh shell 不保留工作目录，使用相对仓库根的完整路径。

## 关键决策记录

对话中做出的关键决策（含命名论证与边界界定）：

1. **security 英文名：`security-engineering` 而非 `software-security`**。理由：① 中文「网络安全」在中文语境泛指整个信息安全，与「安全工程」全链路范畴一致，而 software-security 只覆盖软件层；② 「xx工程（以机为主）」与 `data-engineering`、`knowledge-engineering`、`agent-engineering` 风格同构；③ 与领域 README 已写边界自洽。随后中文名「网络安全 → 安全工程」与英文完全对齐。
2. **docs 英文名：`document-engineering` 而非 `documentation-engineering`**。用户指出 Document Engineering 是更常用术语（单数 Document），采纳后 4 个配套仓库更名并全库清零旧名。
3. **health 领域边界按对象维度组织**：个人（全面管理）/ 家庭（大病管理为主）/ 企业（共同问题管理，如知识工作过疲劳）/ 健康数据安全（底线，与安全工程协同）。
4. **统一规范三原则**（本对话最重要的产出）：
   - **P1 统一规范**：所有领域第二大脑遵循同一信息架构（`data/` 陈述性记忆 + `docs/` 程序性记忆 + `apps/` + `packages/` + `examples/`）；
   - **P2 信息集中**：领域第二大脑是该领域信息唯一集中点，`qtcloud-*` 云产生的数据回流领域档案（数据闭环）；
   - **P3 关联分析**：经统一命名与契约建立跨领域关联（如 安全工程 ↔ 密码管理 ↔ 身份认证 的密钥治理链路）。
   - 落地文档：根 README（新增「统一规范」小节）、ROADMAP（0.6.x/1.0.0 目标）、AGENTS（核心架构思想第 4 条）、各领域 `data/intention`（产品意图按三原则重写）、契约补 `relations:`。
5. **asset studio 规划模式（资产浏览）**：参照 qtfounder studio 的 asset 页面设计——**页面结构 = 仓库目录结构（契约驱动目录镜像）**：资产契约（定义 levels / naming / ignore）→ 资产目录引擎（读契约 → 遍历 → 解析命名 → 排序 → 输出树）→ 通用资产页面（一级 = 资产类型，二级 = 阶段/子类，文件名即条目）；只读浏览、不发明视图、新增资产 = 新增契约（零代码）。
6. **产品应用与领域云两个层级**：qtcrowd / qtdocs 是既有产品实现，`qtcloud-crowd` / `qtcloud-docs` 是领域配套云，领域仓库统一承载领域知识；产品应用可挂入领域 `apps/` 共用。
7. **领域定义文档结构**（回合 8 确立的模板）：概述（一句话定位）→ 领域边界（能力域表）→ 与相邻领域的分工（块引用）→ 子模块现状与规划。与相邻领域的分工是定义里最关键的部分，让「某个实践放哪个仓库」可判定。

## 总结

### 场景判定

调查现状后判定本次初始化属于哪种场景：

- **新建领域第二大脑**：`domains/{name}` 全套仓库不存在 → 主流程（活动一至八）
- **资产聚合容器**：`assets/{name}` 聚合容器重建或新建 → 活动一 + 容器流程
- **已有仓库补全**：仓库成熟但 README 为 stub / 缺 LICENSE → 活动一 + 补全流程
- **挂载已有产品仓库**：产品应用仓库挂入领域 `apps/` → 挂载流程
- **英文更名**：命名需修正 → 更名流程
- **配套追加 / 其他形态**（配套三仓、data 三件套、意图仓库、官网前台、发布流程）：见「对话流程总览 · 其他可复用流程模式」

### 命名惯例

**命名规则**：

- 中文名：四字最佳——「xx管理」（以人为主，如 密码管理 / 健康管理 / 创业管理）、「xx工程」（以机为主，如 安全工程 / 数据工程 / 文档工程），或「xx设计」（如 交互设计）
- 英文名：单数形式，以主体性质决定后缀，`{name}-management` 或 `{name}-engineering`（如 `security-engineering`、`document-engineering`、`crowdsourcing-management`）
- 缩写：市场通用缩写；英文名**超 8 字母才缩写**，否则直接用原名（`sec`、`ixd`、`docs`、`crowd`、`entrep`；`alliance` 恰 8 字母未缩写）
- 命名先例复用：新领域优先沿用体系内既有缩写与风格（如交互设计沿用代码库既有 `ixd`）
- 配套仓库后缀与英文全名一致（更名时需同步改名 GitHub 仓库与所有引用）

**仓库命名模式**：

| 角色 | 领域仓库内路径 | GitHub 仓库名模式 | 实例 |
|------|---------------|-------------------|------|
| 领域仓库 | `domains/{name}`（主仓库子模块） | `quanttide-{name}` | `quanttide-security` |
| 应用云 | `apps/` | `qtcloud-{name}` | `qtcloud-security` |
| 工具集 | `packages/` | `{name}-toolkit` | `quanttide-security-toolkit` |
| 实验室 | `examples/default` | `quanttide-laboratory-of-{english-name}` | `quanttide-laboratory-of-security-engineering` |
| 语境 | `data/context` | `quanttide-context-of-{english-name}` | `quanttide-context-of-security-engineering` |
| 日志 | `data/journal` | `quanttide-journal-of-{english-name}` | `quanttide-journal-of-security-engineering` |
| 意图 | `data/intention` | `quanttide-intention-of-{english-name}` | `quanttide-intention-of-security-engineering` |

**领域仓库统一结构**（统一规范 P1 的落点）：

```text
domains/quanttide-{name}/
├── apps/qtcloud-{name}/        # 可部署应用（云）
├── packages/{name}-toolkit/    # 共享工具集
├── examples/default/           # 实验室
├── data/                       # 陈述性记忆（context/insight/intention/journal/profile/report/roadmap 等 11 类）
└── docs/                       # 程序性记忆（bylaw/essay/gallery/handbook/specification/tutorial 等 6 类）
```

### 分层提交模式

所有场景共用同一提交模式：**子模块 → 领域/容器仓库 → 根仓库，逐层提交推送（提交即推送）**。

- 领域仓库提交：`chore: 初始化<中文名>领域仓库（注册配套子模块）`
- 根仓库提交：`feat: 新增<中文名>领域（<仓库名>）`
- 指针更新提交：`chore: 更新 <父仓库> 子模块指针（<原因>）`

### 注意事项

- **先调查后动手**：避免重复创建仓库（HTTP 422）或破坏已有内容
- **远端冲突**：推送被拒时先 `git pull --rebase`，不要强推（对话中 rebase 合并过 26 个并行提交）
- **契约优先**：`.quanttide/agent/contract.yaml` 要求用户确认的操作（git push、删除、改契约）先列清单等确认
- **减法优先**：删除无效内容优先于新增；不确定的内容宁可空着
- **文档与事实一致**：README 子模块表与实际 `.gitmodules` 对齐（对话中曾误写不存在的 `data/context` 后修正）
- **并行协作安全**：根仓库工作区可能有并行待办，只用 `git add` 具体路径，禁止 `git add -A`
- **共享仓库双挂载**：同一仓库被多个父仓库挂载时（如 qtcrowd 挂 quanttide-crowd 与 quanttide-tech），各父仓库是独立克隆，需分别更新指针

## 关联

- 循环范式：[loops](../loops/README.md)
- 提交规范：devops-commit
- 子模块操作：devops-submodule
