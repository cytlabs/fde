---
name: fde-mvp-scoping
description: Use when narrowing a validated business problem and AI opportunity into a 1-2 week MVP scope, defining the end-to-end loop, core functions, non-goals, human review points, risk boundaries, validation criteria, and next actions.
---

# FDE MVP Scoping

## 核心目标

把已经确认的业务问题和候选 AI 机会，收敛成 1-2 周内可演示或可交付的 MVP 闭环。

## 使用时机

- 用户已经有业务流程、痛点和候选场景。
- 用户想确定第一阶段做什么、不做什么。
- 用户需要定义输入、处理、人工审核、输出和反馈闭环。

## 不使用时机

- 用户还没讲清业务背景：使用 `fde-intake`。
- 用户还没还原流程：使用 `fde-workflow-mapping`。
- 用户还没判断 AI 机会：使用 `fde-ai-opportunity-assessment`。
- 用户只想写客户材料：使用 `fde-solution-brief`。

## 强规则

- MVP 必须有明确输入、处理、人工审核、输出和业务反馈。
- 不要把长期愿景塞进第一阶段。
- 高风险决策不得全自动。
- 没有验收方式的功能不进入 MVP。
- 必须明确非 MVP 范围。

## 工作流程

1. 复述核心业务问题。
2. 选择一个最小可验证场景。
3. 定义 MVP 闭环。
4. 列出核心功能和非 MVP 范围。
5. 明确人工审核节点、风险边界和验收标准。
6. 输出下一步行动。

## 输出格式

````markdown
## 核心业务问题

...

## MVP 闭环

```text
输入 -> AI/自动化处理 -> 人工审核 -> 输出 -> 业务反馈
```

## 核心功能
1. ...
2. ...
3. ...

## 非 MVP 范围
- ...

## 人工审核节点
- ...

## 风险边界
- ...

## 验收标准
- ...

## 下一步行动
1. ...
2. ...
3. ...
````

## 质量检查

- 是否能在 1-2 周内演示或交付？
- 是否闭环清晰？
- 是否明确非 MVP 范围？
- 是否保留人工审核？
- 是否有可验证的验收标准？
