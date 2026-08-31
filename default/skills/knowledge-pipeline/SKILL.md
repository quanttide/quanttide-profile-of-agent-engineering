---
name: knowledge-pipeline
description: 知识生产流水线,将仓库、日志、工作语境等原始材料加工为结构化知识文档(quick-view/intention/insight/roadmap)。运行前自动检查并初始化第二大脑标准目录结构。
---

# 知识生产流水线

严格按 **5 阶段全局生命周期 (Lifecycle SOP)** 执行：

## 全局生命周期流水线 (5-Stage Lifecycle SOP)

### 阶段 1：环境识别与目录就绪 (Phase 1: Boot & Readiness)

- **架构约束**：双九宫格是**领域级聚合仓库**组织坐标系，严禁向叶子代码仓库套娃注入九宫格。
- **命名规范与角色判定**：
  - **领域第二大脑 / 既有九宫格工作区**：符合命名契约（`quanttide-{领域短名}` 如 `quanttide-data`），或**根目录已包含双九宫格核心目录**（如已存在 `data/` 与 `docs/`）：唯一挂载点，必须执行 20 类标准目录检查与幂等初始化。
  - **具体资产子仓库 / 叶子节点**（Platform: `qt*` / `qtcloud-*`、Toolkit: `*-toolkit`、Example: `*-laboratory-*`、单项资产: `quanttide-{资产}-of-{领域}`，且无既有双九宫格）：严禁套娃初始化九宫格，产物只路由至外部知识库。
- **20 类标准资产目录**：
  - **陈述型（11 类）**：`data/{context,archive,report,library,history,journal,profile,brochure,roadmap,insight,intention}/`
  - **程序型（6 类）**：`docs/{bylaw,specification,handbook,gallery,tutorial,essay}/`
  - **规则引擎友好（3 类）**：`apps/` (Platform), `packages/` (Toolkit), `examples/` (Example)
- **初始化与门禁**：领域大脑缺失目录立即递归创建并补 `.gitkeep`，已存在跳过；逐项报告检查结果，确认就绪方可进入阶段 2。

### 阶段 2：工作流路由与意图锁定 (Phase 2: Route & Intent Lock)

- **路由匹配**：透视仓库 → **WF1** | 整理工作意图 → **WF2** | 整理工作洞察 → **WF3** | 更新路线图 → **WF4**。
- **阶段门禁**：向用户明确反馈锁定的工作流名称，严禁擅自跨工作流或跳步执行。

### 阶段 3：交互式输入摄入 (Phase 3: Interactive Ingestion Barrier)

- **阻断提问**：严格使用工作流定义的标准话术**停下来向用户逐项提问**；严禁假定或默认扫描。
- **通读校验**：收到路径后调用 `Read` 通读内容；路径不存在或为空时必须报错并等待用户重输。

### 阶段 4：受约束内容生成 (Phase 4: Constrained Synthesis)

- **读取模板**：读取 `assets/*.md` 模板，严格遵循对应工作流的骨架与字段定义：
  - **WF1**：包含顶层树、关键文档表、层级 Mermaid 图、模块职责机制与命令速查；
  - **WF2**：恰好 3 条意图，每条绑定日志与代码双证据、交付目标、设计排除与核心原则；
  - **WF3**：严格五段式（情景导入、核心模型/公式、分层递进[假设-矛盾-解法]、价值升华、总结收束）；
  - **WF4**：恰好 3 个同构需求（现状+后果、3 目标、3 技术方向），Mermaid 依赖节点文本强制使用双引号 `["..."]`。
- **语言与排版规范**：
  - 全篇用词专业、言简意赅，严禁空话套话与多余修辞；
  - **各级标题与任何正文段落、有序/无序列表、代码块、表格之间必须严格保留一行空行分隔，严禁紧贴粘连**。

### 阶段 5：落盘前 5 项硬门禁自检与路径确认 (Phase 5: Pre-commit Self-Audit & Confirmation)

在调用写入工具前必须通过 5 项自检：
1. **[注释清洁]** 彻底剔除所有 HTML 注释（`<!-- ... -->`）、占位符及说明文字。
2. **[复选框清洁]** 正文中绝无任何未勾选的复选框（`- [ ]`）。
3. **[排版空行清洁]** 确认所有标题、段落、列表、代码块之间均严格保留了一行空行分隔。
4. **[篇幅与结构硬顶]** 严格符合对应工作流限制（WF1 ≤ 300行 | WF2 ≤ 50行且恰好3条 | WF3 ≤ 80行且五段式 | WF4 ≤ 100行且3同构需求+防御性Mermaid）。
5. **[输出路径确认]** 计算建议路径并向用户提问确认（“建议输出路径为 `<建议路径>`，是否确认写入？”），等待确认。
- **交付**：自检与确认通过后落盘并交付总结。

---

## 工作流规格定义

| 工作流 | 阶段 3 输入项（标准提问话术） | 阶段 4 模板 | 阶段 5 建议输出路径 | 篇幅与结构硬顶 |
| :--- | :--- | :--- | :--- | :--- |
| **WF1: 项目透视 (quick-view)** | 1. “请输入要分析的目标仓库/项目路径（例如：`repo/<仓库名>` 或 `apps/<产品名>`）：” | `assets/quick-view.md` | `data/profile/<目标仓库名>-quick-view.md` | ≤ 300 行<br>（含 Mermaid 图） |
| **WF2: 工作意图 (intention)** | 1. “请输入要分析的工作日志文件夹路径（建议默认：`data/journal/`）：”<br>2. “请输入已有工作意图文件夹路径（建议默认：`data/intention/`）：”<br>3. “请输入关联代码仓库路径（例如：`repo/<代码仓库名>` 或 `apps/<产品名>`）：” | `assets/intention.md` | `data/intention/<代码仓库名>-intention.md` | ≤ 50 行<br>（恰好 3 条+双证据） |
| **WF3: 工作洞察 (insight)** | 1. “请输入要分析的工作语境文件路径（例如：`data/context/<文件名>.md`）：” | `assets/insight.md` | `data/insight/<工作语境名>-insight.md` | ≤ 80 行<br>（严格五段式） |
| **WF4: 工作路线图 (roadmap)** | 1. “请输入工作意图文件路径（例如：`data/intention/<代码仓库名>-intention.md`）：”<br>2. “请输入工作洞察文件路径（例如：`data/insight/<文件名>-insight.md`）：”<br>3. “请输入关联代码仓库路径（例如：`repo/<代码仓库名>`）：”<br>4. “请输入现有工作路线图文件路径（若为从零创建请输入 `none`；已有如：`data/roadmap/<代码仓库名>-ROADMAP.md`）：” | `assets/ROADMAP.md` | `data/roadmap/<代码仓库名>-ROADMAP.md` | ≤ 100 行<br>（3同构需求+带引号Mermaid） |
