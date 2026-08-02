# 循环（Loops）

从实践日志（journal）中提取的**循环范式**记录。档案记录的就是各种 harness 的技巧、循环、约束，其中循环是最核心的形态。

## Loop 范式

> 先从人类的视角出发，然后再回到人类的视角，中间把复杂的部分交给机器自己去做。

## Loop 与 Workflow 的区别

- **workflow** 单次就能做完，处理不了动态的情况
- **loop** 的关键是**反馈点**——一次循环过后需要与人交互一下，然后再进行下一次循环
- 很多情况像 workflow，但需要知道循环的反馈点在哪里，这正是 loop 区别于 workflow 的地方

## 承载方式

- 一个 loop 需要一个流程来承载，哪怕只是一个简单的 SH 脚本或 Python 脚本
- 可以用 Markdown 把 harness 写成 loop，叫 loop engineering
- 需要在 PI 的基础上进行封装

## 目录

| 循环 | 说明 |
|------|------|
| [devops-code.md](devops-code.md) | 开发循环：文档驱动 + 测试驱动 + 评审重构 |
| [devops-plan.md](devops-plan.md) | 规划循环：intention → insights → roadmap |
