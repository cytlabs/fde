---
name: fde-mvp-scoping
description: Narrow one validated business pain and evidence-backed AI or automation opportunity into a 1-2 week MVP. Use when the workflow, input, output, data access, review owner, and main risks are known enough to define scope, non-goals, technical path, baseline, target, evaluation sample, acceptance owner, and next actions. Do not use for vague transformation goals or unvalidated opportunities.
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
- 不得用没有基线、样本或验收责任人的百分比作为验收目标。

## 工作流程

1. 复述核心业务问题。
2. 选择一个最小可验证场景。
3. 定义 MVP 闭环。
4. 列出核心功能和非 MVP 范围。
5. 选择最小技术路径，优先复用现有工具和可导出的真实样例。
6. 明确人工审核节点、风险边界和验收标准。
7. 输出下一步行动。

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

## 技术路径
- 现有系统/数据入口：
- MVP 处理方式：
- 输出回写或交付方式：
- 暂不建设的集成：

## 风险边界
- ...

## 验收标准
| 指标 | 当前基线 | MVP 目标 | 测试样本 | 测量方式 | 验收责任人 |
| --- | --- | --- | --- | --- | --- |

## 失败判定
- 数据问题：...
- 模型/规则问题：...
- 流程或采用问题：...

## 已确认与待确认
- 已确认事实：...
- 当前假设：...
- 待补证据：...

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
