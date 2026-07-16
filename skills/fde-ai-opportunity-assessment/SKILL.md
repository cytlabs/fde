---
name: fde-ai-opportunity-assessment
description: Assess evidence-backed workflow steps or candidate scenarios for AI, deterministic workflow automation, agents, RPA, traditional systems, or manual process improvement. Use when inputs, outputs, pain, data, reviewability, and risks can be evaluated. Do not use when the business context or current workflow is still unknown, or when the user only wants interview questions or final MVP scope.
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
- 高业务价值不能抵消不可审核的高风险或不可获得的数据。
- 必须使用下方完整模板。不得用“高/中/低”“适配度”或自定义表格替代 1-5 分及证据。
- 每个候选路径都要逐项评分；未知项写 `待验证`，不得省略评分维度或交接字段。

## 评估口径

每个维度使用 1-5 分，并写出证据；缺少证据时标记 `待验证`，不得用猜测补分。

- **业务价值**：1 为影响不明确，5 为直接影响已量化核心指标。
- **输入/输出清晰度**：1 为依赖隐性判断，5 为边界和格式稳定。
- **数据可得性**：1 为无样例或无权限，5 为有权限、历史样例和质量记录。
- **可审核性**：1 为结果难复核，5 为可低成本逐条审核或自动校验。
- **MVP 可行性**：1 为依赖重大系统改造，5 为 1-2 周可用真实样例跑通。

硬性门槛：无合法数据路径、错误不可发现且影响重大、或必须无人工全自动时，标记 `暂不建议`，不计算为高优先级。

## 工作流程

1. 列出候选场景或流程环节。
2. 评估频率、业务价值、输入清晰度、输出清晰度、数据可得性、人工审核、风险。
3. 判断适合 AI、Workflow、Agent、RPA、传统系统还是暂不自动化。
4. 输出优先级和与 FDE 继续确认的问题。

## 输出格式

```markdown
## AI 机会评估

| 场景 | 价值 | 输入输出 | 数据 | 可审核性 | MVP | 风险 | 证据强度 | 推荐路径 | 优先级 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

评分格式：`分数/5：证据或待验证项`。证据强度仅使用 `已验证` / `有迹象` / `纯假设`。

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

## 交接到 MVP
- 推荐场景：
- 已确认输入和输出：
- 可用数据和样例：
- 人工审核人：
- 主要风险：
- 待验证假设：
```

## 质量检查

- 是否基于流程和痛点判断，而不是基于工具偏好？
- 是否明确输入、输出、数据和审核？
- 是否区分了 AI、Workflow、Agent、RPA、传统系统和流程优化？
- 是否指出了高风险和暂不优先的场景？
