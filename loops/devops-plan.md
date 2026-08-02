# 规划循环

典型的规划性 loop：从**想法到落实**的过程。

```
intention → insights → roadmap
```

## 说明

- 从意图（intention）出发，经过洞察（insights），落实到路线图（roadmap）
- 与开发循环不同，规划循环的反馈点在于：一次循环之后与人类交互，确认意图与洞察是否符合预期，再进入下一次循环

## 验收标准

产物清单（详见 [README.md](README.md) 验证章节）：

| # | 阶段 | 产物 | 达标要求 |
|---|------|------|---------|
| 1 | intention | `intention.md` | 意图明确可表述 |
| 2 | insights | `insights.md` | 洞察来自实践/数据，非凭空 |
| 3 | roadmap | `roadmap.md` | 可执行、有阶段、可回查 |

校验方式：`devops-plan.sh <任务目录> --check`，产物缺失则本轮未完成（exit 1）。
