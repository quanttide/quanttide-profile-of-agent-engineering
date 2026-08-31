# qtcloud-data 工作意图

## 1. 对象存储资产治理与单向数据湖流转
- **背景/动机**：统一多端碎片化数据资产，实现非结构化到结构化资产的单向晋级流转。
- **关键证据**：
  - 日志：`data/journal/default/2026-07-28.md:29-55` 确立对象存储命名规范与私有到公开流转
  - 代码：`src/cli/src/storage/` 与 `src/stage/transfer.rs:transfer` 存储抽象与传输分发
- **参考对标**：Lakehouse 分层架构与 DVC 数据版本管理
- **设计实现**：
  - **平台/模块**：`src/storage/` 存储扩展与 `src/stage/transfer.rs`
  - **交付目标**：支持标准 S3 命名规范分发，实现 `qtdata-private` 到 `qtdata-provider` 的自动化校验与同步
- **设计排除**：暂不自研元数据编排引擎，优先复用现有对象存储协议
- **核心原则**：资产单向流动，非结构化向规范化不可逆流转

## 2. CLI 获客驱动的 Provider 托管执行与计量审计
- **背景/动机**：落实“CLI 免费获客，服务端托管执行按次计量”的商业化落地路径。
- **关键证据**：
  - 日志：`data/intention/business-model.md:9-22` 托管执行按次计量模式与报告付费终点
  - 代码：`src/cli/ROADMAP.md:40-42` CLI 配置 `PROVIDER_URL` 与 Blueprint 远程 run 调用
- **参考对标**：Modal 按秒计费与 Posit Cloud 统计环境托管
- **设计实现**：
  - **平台/模块**：`src/stage/process.rs` 与 `POST /blueprints/{name}/runs`
  - **交付目标**：CLI 支持 `--remote` 参数调用 Provider 托管执行并返回 Job 计量数据
- **设计排除**：不做复杂的 Databricks 多档位混合席位计费，仅按 run 统一结算
- **核心原则**：AI 生成与统计计算均作为统一 run resource 纳入单次透明计量

## 3. 蓝图异常预设与非技术可读交付质量报告
- **背景/动机**：消除商务谈判与技术实施的认知断层，提供可视化的质量与交付凭据。
- **关键证据**：
  - 日志：`data/journal/default/2026-07-27.md:29-78` 蓝图异常策略预设与交付质量报告
  - 代码：`src/cli/src/spec/blueprint.rs` 与 `src/implementation/catalog.rs`
- **参考对标**：OpenMetadata 数据契约质量看板
- **设计实现**：
  - **平台/模块**：`src/output.rs` 与 `src/spec/blueprint.rs`
  - **交付目标**：支持 Blueprint 异常策略结构化导出与 Catalog 验收质量达标卡片渲染
- **设计排除**：暂不开发复杂多人实时在线协同批注，优先提供静态 Markdown 报告
- **核心原则**：以数据契约为唯一事实源，交付报告作为最终价值闭环
