# 领域第二大脑初始化上下文（second-brain-init）

从「领域第二大脑初始化」实践对话中提取的**初步逻辑**，用于沉淀为 Skill 与 harness。本文档是上下文工程的中间产物——先把原始对话整理为可复用逻辑，再据此产出自动化能力。

文档按 **原始对话 → 初步逻辑 → Skill/harness** 组织：主体是初步逻辑（各逻辑单元标注可沉淀的产出物），末尾保留对话索引供回溯，避免原始记录淹没逻辑本身。

> 交付形态原则：沉淀产物贴近操作清单而非流程描述，先做最小可用版本再迭代（源自回合 26–27 删除 asset-init 技能的教训）。

## 场景定位

「领域第二大脑初始化」覆盖新建领域第二大脑、补全既有仓库、重建聚合容器、挂载产品仓库、英文更名等实践。动手前先调查现状判定场景，再选处理路径。

- **新建领域第二大脑**：`domains/{name}` 全套仓库不存在，走标准流程
- **资产聚合容器**：`assets/{name}` 容器重建或新建，走容器流程
- **已有仓库补全**：仓库成熟但 README 为 stub 或缺 LICENSE，走补全流程
- **挂载已有产品仓库**：产品应用仓库挂入领域 `apps/`，走挂载流程
- **英文更名**：命名需修正，走更名流程
- **配套追加**：配套三仓、data 三件套、意图仓库、官网前台、发布流程等，见变体流程

## 命名逻辑

可沉淀为「命名助手」Skill。规则要点：

- **中文名**：四字最佳。「xx管理」以人为主（密码管理/健康管理/创业管理），「xx工程」以机为主（安全工程/数据工程/文档工程），「xx设计」如交互设计
- **英文名**：单数形式，以主体性质决定后缀，`{name}-management` 或 `{name}-engineering`
- **缩写**：市场通用缩写；英文名超 8 字母才缩写，否则直接用原名（`sec`、`ixd`、`docs`、`crowd`、`entrep`；`alliance` 恰 8 字母未缩写）
- **先例复用**：新领域优先沿用体系内既有缩写与风格（如交互设计沿用 `ixd`）
- **配套仓库后缀**：与英文全名一致，更名时需同步 GitHub 仓库与所有引用

仓库命名模式：

| 角色 | 领域仓库内路径 | GitHub 仓库名模式 | 实例 |
|------|---------------|-------------------|------|
| 领域仓库 | `domains/{name}` | `quanttide-{name}` | `quanttide-security` |
| 应用云 | `apps/` | `qtcloud-{name}` | `qtcloud-security` |
| 工具集 | `packages/` | `{name}-toolkit` | `quanttide-security-toolkit` |
| 实验室 | `examples/default` | `quanttide-laboratory-of-{english-name}` | `quanttide-laboratory-of-security-engineering` |
| 语境 | `data/context` | `quanttide-context-of-{english-name}` | `quanttide-context-of-security-engineering` |
| 日志 | `data/journal` | `quanttide-journal-of-{english-name}` | `quanttide-journal-of-security-engineering` |
| 意图 | `data/intention` | `quanttide-intention-of-{english-name}` | `quanttide-intention-of-security-engineering` |

领域仓库统一结构（统一规范 P1 的落点）：

```text
domains/quanttide-{name}/
├── apps/qtcloud-{name}/        # 可部署应用（云）
├── packages/{name}-toolkit/    # 共享工具集
├── examples/default/           # 实验室
├── data/                       # 陈述性记忆（context/insight/intention/journal/profile/report/roadmap 等 11 类）
└── docs/                       # 程序性记忆（bylaw/essay/gallery/handbook/specification/tutorial 等 6 类）
```

## 标准流程

可沉淀为「资产初始化」harness（loop）。「全新领域第二大脑」标准流程，每轮结束须人工确认再继续（反馈点）：

1. **先调查后动手**：检查 GitHub 是否已有同名仓库，查看最近创建领域的结构作模板，确认中文名/英文名/缩写（不确定先问，用户不回应按命名规则取默认）。命令 `gh repo view quanttide/<repo> --json name`
2. **创建 GitHub 仓库**（全部公开）：领域仓库 + 应用云 + 工具集 + 实验室 + data 三件套（语境/日志/意图），共 7 个，均带 README 初始提交。命令 `gh repo create quanttide/quanttide-{name} --public --add-readme`
3. **注册子模块**：`git submodule add`，领域仓库内路径约定 `apps/qtcloud-{name}`、`packages/{name}-toolkit`、`examples/default`、`data/{context,journal,intention}`
4. **编写领域仓库骨架**：README（概述 + 领域边界 + 相邻领域分工 + 子模块表 + 许可）、LICENSE、CHANGELOG（`[0.1.0]` 初始化记录）。减法优先，只放骨架
5. **分层提交推送**（提交即推送）：子模块 → 领域仓库 → 根仓库
6. **根仓库注册**：`domains/README.md` 三处（目录结构 + 领域清单行 + 领域项目小节）、根 `README.md`（领域数量 +1）、根 `CHANGELOG.md`
7. **验证**：子模块指针与各 HEAD 一致、主仓库与远端同步、无残留未提交项

操作检查清单：

- 动手前先 `gh repo view` 检查仓库是否已存在
- 不确定领域名先向用户确认，用户不回应则按命名规则取默认
- 只 `git add` 具体路径，禁止 `git add -A`
- 推送被拒先 `git pull --rebase`
- 按「子模块 → 领域仓库 → 根仓库」分层提交，提交即推送
- 所有用户可见变更同步更新 CHANGELOG；ROADMAP 等规划类不记
- 完成后验证指针一致、工作区干净、与远端同步

## 变体流程

可沉淀为 harness 分支。各变体的具体命令见原始材料，此处给操作要点：

- **配套三仓追加**：为已建领域补 `apps/`、`packages/`、`examples/default` 并注册
- **data 三件套追加**：补 `data/context`、`data/journal`，按需补 `data/intention`
- **意图仓库**：主文档 `index.md` = 背景与动机 → 统一框架 → 云模块设计 → 建设路径；素材取自 journal 与产品思路
- **已有仓库补全**：先调查现状（是否成熟、README 是否 stub、缺什么），再按类型处理（补全领域定义 / 重建聚合容器）
- **聚合容器初始化**：能力轴容器参照同类容器组织，注册既有 `-of-{name}` 系列，许可证参照同类容器（容器 Apache 2.0，领域 CC BY 4.0）
- **产品应用挂载**：既有产品应用与领域配套云是两个层级；挂入 `apps/` 时保持 README 子模块表与 CHANGELOG 同步
- **官网前台初始化**：`src/site` = Vite + React + TypeScript，页面内容源自产品意图档案，构建与 lint 验证通过再提交
- **发布流程**：预检查 → 固化 Unreleased → 记录发布日志 → 打标签 → 发布

## 决策规则

可沉淀为「决策」Skill。对话中的关键决策及其论证：

1. **security 命名**：`security-engineering` 而非 `software-security`。理由：中文「网络安全」泛指整个信息安全，software-security 只覆盖软件层；「xx工程（以机为主）」与 `data-engineering`、`agent-engineering` 风格同构；与已写边界自洽
2. **docs 命名**：`document-engineering` 而非 `documentation-engineering`，Document Engineering 是更常用术语
3. **health 边界**：按对象维度组织，个人（全面管理）/ 家庭（大病管理为主）/ 企业（共同问题管理）/ 健康数据安全（底线，与安全工程协同）
4. **统一规范三原则**：
   - P1 统一规范：所有领域第二大脑遵循同一信息架构（`data/` 陈述性记忆 + `docs/` 程序性记忆 + `apps/` + `packages/` + `examples/`）
   - P2 信息集中：领域第二大脑是该领域信息唯一集中点，`qtcloud-*` 云数据回流领域档案
   - P3 关联分析：经统一命名与契约建立跨领域关联
5. **asset studio 规划**：页面结构 = 仓库目录结构（契约驱动目录镜像），资产契约 → 目录引擎 → 通用页面，只读浏览、不发明视图，新增资产 = 新增契约（零代码）
6. **产品应用与领域云**：qtcrowd/qtdocs 是产品实现，`qtcloud-crowd`/`qtcloud-docs` 是领域配套云，产品应用可挂入领域 `apps/` 共用
7. **领域定义文档结构**：概述（一句话定位）→ 领域边界（能力域表）→ 相邻领域分工（块引用）→ 子模块现状与规划。相邻领域分工最关键，使「某个实践放哪个仓库」可判定

## 格式与契约

可沉淀为「格式校验」Skill。读取到的三类契约（全文见原始材料）：

- **文档工程契约**（`.quanttide/docs/contract.yaml`）：最多 3 级标题、文档标题 h1、代码块必须标语言（围栏式）、文件名小写、目录名复数。配套「文档格式技能」补充：尽量少用表格与加粗、中文引号使用「」
- **数字资产契约**（`.quanttide/asset/contract.yaml`）：按能力轴 + 领域轴组织，与 `.gitmodules` 对齐，条目字段 `title/type/category/audience/path/description`；演进方向为补 `structure:` 与 `relations:` 使统一框架机器可读
- **AI 执行审核契约**（`.quanttide/agent/contract.yaml`）：带契约限制的仓库，需审核操作（删除/推送/改契约等）先列清单等确认；读取类与普通写文档免审

## 提交与协作规范

- **CHANGELOG**：Keep a Changelog 格式；新领域写完整 `[0.1.0]` 初始化记录；常规变更记 `[Unreleased]`；对用户可见变更须更新，ROADMAP 等规划类不记（最小干预）
- **许可证**：领域仓库一律 CC BY 4.0；资产/能力轴容器用 Apache 2.0；既有成熟应用保留原许可证
- **提交信息**：领域与根仓库用 Conventional Commits（中文描述）；日志仓库按惯例用日期
- **分层提交 / 提交即推送**：子模块 → 领域仓库 → 根仓库逐层提交推送，禁止越级；子模块文件在子模块内提交，父仓库只更新指针
- **并行协作安全**：只用 `git add` 具体路径，禁止 `git add -A`；远端被拒先 `git pull --rebase`；子模块 detached HEAD 先 `git checkout main`
- **读写纪律**：每回合编辑前先 read；fresh shell 用相对仓库根的完整路径

## 产出物清单

由本文档初步逻辑映射的 Skill 与 harness：

| 初步逻辑 | 产出物 | 形态 | 状态 |
|---------|--------|------|------|
| 命名逻辑 | 命名助手 | Skill | 待沉淀 |
| 标准流程 | 资产初始化循环 | harness | 待沉淀 |
| 场景判定 | 场景判定 | Skill | 待沉淀 |
| 决策规则 | 领域定义决策 | Skill | 待沉淀 |
| 格式与契约 | 格式校验 | Skill | 待沉淀 |

## 原始材料索引

去敏后的对话回合简表，供回溯原始对话，非正文（`secret` 指「密码管理」领域，非密钥）：

| 回合 | 用户指令（实质内容） | 关键动作与结果 |
|------|---------------------|----------------|
| 1 | 创建领域第二大脑 quanttide-secret | 确认中文名「密码管理」；创建领域仓库骨架，注册主仓库子模块，登记领域清单 |
| 2 | 创建 qtcloud-secret / toolkit / laboratory | 确立「应用 + 工具集 + 实验室」三配套模式 |
| 3 | 创建 quanttide-security | 按同流程创建安全领域骨架 |
| 4–5 | 为 security 创建三配套仓库 | 实验室先按 `-of-software-security` 命名 |
| 6 | software-security vs security-engineering | 确定 security-engineering 更合适，执行更名 |
| 7 | 网络安全 → 安全工程 | 全链路同步中文名 |
| 8 | 如何定义这个领域 | 形成领域定义模板并落盘 README |
| 9 | 提交所有更新 | 批量提交推送子模块指针，工作区干净 |
| 10 | 创建 data/context 和 journal | 确立 data 仓库命名模式 |
| 11 | 主仓库发布 patch | 按发布流程发布 |
| 12 | 统一规范核心思想，记录到 journal | 整理语音为结构化日志（先 pull） |
| 13 | 领域第二大脑产品思路如何更新 | 提出三原则与三层文档落实清单，反复收敛 |
| 14 | 更通俗解释 | 大白话复述统一规范 |
| 15 | yes | 落地三份元文档 + 安全工程意图仓库范例 |
| 16–20 | 初始化 quanttide-health | 创建健康管理领域，边界按对象维度 |
| 21–22 | 初始化 quanttide-asset + studio 规划 | 补全领域定义，Studio 规划写入 ROADMAP，澄清 CHANGELOG |
| 23 | 创建 quanttide-design | 全套创建交互设计领域，缩写 `ixd` |
| 24 | 初始化 quanttide-profile | 重建聚合容器，聚合 12 个 `profile-of-*` 仓库 |
| 25 | 更新 quanttide-product profile | 新增 qtcrowd 条目 |
| 26–27 | 写 asset-init 技能；不好，删除 | 删除并完整回滚（交付形态教训） |
| 28 | 创建 quanttide-entrep | 创业管理全套创建 |
| 29 | 创建 quanttide-alliance | 联盟管理，放「沟通与管理」组 |
| 30 | 创建 quanttide-crowd | 众包从产品应用提升为独立领域 |
| 31 | qtcrowd 加入 apps/ | 产品应用挂入领域 |
| 32 | qtcrowd 初始化 src/site | 官网脚手架三页，构建验证 |
| 33 | yes | 收尾遗留事项 |
| 34 | 初始化 quanttide-media | 成熟仓库补全领域定义 + 许可 |
| 35 | 创建 quanttide-docs | 复用 toolkit，新建其余 6 仓 |
| 36 | Document Engineering 更常用 | 4 个配套仓库更名并全库清零 |
| 37 | yes | qtdocs 挂入文档工程领域 `apps/` |

## 关联

- 循环范式：[loops](../../default/loops/README.md)
- 提交规范：devops-commit
- 子模块操作：devops-submodule
