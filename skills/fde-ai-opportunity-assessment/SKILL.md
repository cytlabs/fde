---
name: fde-ai-opportunity-assessment
description: Use when assessing whether workflow steps or candidate business scenarios are suitable for AI, workflow automation, agents, RPA, traditional systems, or manual process improvement based on input clarity, output clarity, data availability, reviewability, risk, and short-term MVP feasibility.
---

# FDE AI Opportunity Assessment

## 核心目标

判断业务流程中的哪些环节适合 AI 或自动化提效，哪些不适合当前优先做，并明确原因、风险和前置条件。

## 使用时机

- 用户提供了一个或多个候选 AI 场景。
- 用户已有流程和痛点，希望判断哪些环节适合 AI。
- 用户想比较 AI、Workflow、Agent、RPA、传统系统或人工流程优化。

## 不使用时机

- 用户还没提供业务背景：使用 `fde-intake`。
- 用户还没还原流程：使用 `fde-workflow-mapping`。
- 用户想收敛 1-2 周交付范围：使用 `fde-mvp-scoping`。

## 强规则

- 没有明确输入和输出，不得判断为高优先级 AI 场景。
- 没有数据来源或历史样例，不得假设 AI 效果可验证。
- 高风险场景必须保留人工审核。
- 不要把所有自动化都归为 Agent；必要时建议 Workflow、RPA、传统系统或流程优化。

## 工作流程

1. 列出候选场景或流程环节。
2. 评估频率、业务价值、输入清晰度、输出清晰度、数据可得性、人工审核、风险。
3. 判断适合 AI、Workflow、Agent、RPA、传统系统还是暂不自动化。
4. 输出优先级和与 FDE 继续确认的问题。

## 输出格式

```markdown
## AI 机会评估

| 场景 | 业务价值 | 输入 | 输出 | 数据情况 | 人工审核 | 风险 | 推荐路径 | 优先级 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 推荐优先讨论
- ...

## 可以后续讨论
- ...

## 暂不建议优先做
- ...

## 需要补充的信息
1. ...
2. ...
3. ...
```

## 质量检查

- 是否基于流程和痛点判断，而不是基于工具偏好？
- 是否明确输入、输出、数据和审核？
- 是否区分了 AI、Workflow、Agent、RPA、传统系统和流程优化？
- 是否指出了高风险和暂不优先的场景？
