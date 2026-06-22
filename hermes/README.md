# Hermes Agent 配置参考

从当前系统 Hermes Agent 配置采集。

## 启用的插件

- `ponytail/` — 懒人高级开发模式插件，YAGNI 阶梯规则

### 安装方式

```bash
hermes plugins install https://github.com/neptun-zuti/ponytail-hermes
```

## 当前启用的 Skills

以下 skills 来自当前的 Hermes 配置（`~/.hermes/skills/`），分类见 `skills_list`：

| Skill | 类别 | 用途 |
|-------|------|------|
| `bylaw-from-data` | 章程编写 | 从实际数据反向驱动章程编写 |
| `bylaw-architecture` | 软件工程 | 章程体系方法论 |
| `bylaw-numbering-cascade` | 软件工程 | 章程编号重新编排 |
| `game-design-doc-hierarchy` | 游戏设计 | 游戏文档分层体系 |
| `game-design-prototype-workflow` | 游戏设计 | 游戏设计原型工作流 |
| `narrative-engineering-workflow` | 软件工程 | 三段式 AI 辅助写作 |
| `requesting-code-review` | 软件工程 | 预提交代码审查流水线 |
| `three-layer-doc-alignment` | 软件工程 | 三层次文档对齐发布 |
| `test-driven-development` | 软件工程 | TDD 工作流 |
| + 其他软件工程 skill | | |

> **注意**：Skills 随开发习惯变化较快，本文件仅作参考。最新列表以 `hermes skills list` 为准。
