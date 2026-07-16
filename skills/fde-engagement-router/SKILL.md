---
name: fde-engagement-router
description: Route ambiguous or multi-stage FDE requests to exactly one next skill. Use when the user is unsure which FDE stage applies or mixes intake, interview, workflow mapping, pain analysis, AI opportunity assessment, MVP scoping, and solution brief work. Do not use when the user explicitly requests one stage and has supplied that stage's required inputs.
---

# FDE Engagement Router

## 核心目标

判断当前用户处于 FDE 工作流的哪个阶段，并引导使用正确的阶段型 skill。这个 skill 不做深度业务分析、不输出方案、不替其他 skill 完成工作。

## 阶段路由

- **客户前置收集**：用户还没说清企业背景、业务目标、想解决的问题。使用 `fde-intake`。
- **老板首访 / 商机判断**：用户第一次见老板、创始人、总经理、一把手，或想判断客户是否值得继续投入。使用 `fde-intake`，并读取老板首访 playbook。
- **访谈准备或实时追问**：用户准备访谈、开需求会，或提供客户原话想知道怎么追问。使用 `fde-discovery-interview`。
- **业务流程还原**：用户提供流程口述、会议记录、部门场景，想拆步骤、角色、工具、输入输出。使用 `fde-workflow-mapping`。
- **痛点分析**：用户想区分表层需求、真实痛点、业务影响和关键角色。使用 `fde-pain-analysis`。
- **AI 机会评估**：用户想判断哪些环节适合 AI、Workflow、Agent、RPA 或传统自动化。使用 `fde-ai-opportunity-assessment`。
- **MVP 收敛**：用户已有足够流程和机会信息，想收敛 1-2 周可演示或可交付闭环。使用 `fde-mvp-scoping`。
- **方案表达**：用户想把已确认内容整理成客户可读材料、proposal 或阶段计划。使用 `fde-solution-brief`。

## 强规则

- 不要在 router 中做深度诊断或技术方案。
- 如果用户请求跨多个阶段，先指出阶段顺序，不要一次性混合输出。
- 如果信息不足，先推荐最前置的合适 skill。
- 如果用户明确点名某个 skill，尊重显式选择，但指出可能缺少的前置产物。
- 一次只推荐一个“立即使用”的 skill；其他阶段只能列为后续顺序。
- 必须使用下方完整模板，不得用咨询建议、问题清单或直接分析替代路由结果。
- 信息未知时写 `待确认`，不得因此省略“推荐 skill”或“交接包”。
- 不得在 router 中拟定 MVP、交付物、样本数量或候选功能；这些属于下游阶段。

## 输出格式

```markdown
## 当前阶段判断

...

## 推荐使用的 skill

`skill-name`

## 推荐原因

- ...

## 进入该阶段前需要的信息

- ...

## 交接包

- 已确认事实：...
- 当前假设：...
- 可用证据：...
- 信息缺口：...
- 用户期望产物：...

## 后续阶段

1. ...
2. ...
```

## 质量检查

- 是否只做路由，没有替下游 skill 做分析？
- 是否解释了为什么推荐该阶段？
- 是否指出了缺失的前置信息？
- 是否给出了清晰的下一步？
- 交接包是否能让下一个 skill 直接继续，而不需要重新理解上下文？
