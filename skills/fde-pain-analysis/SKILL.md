---
name: fde-pain-analysis
description: Use when distinguishing a customer's stated solution from the real business pain, analyzing explicit needs, hidden pain points, business impact, affected roles, and assumptions after intake, discovery, or workflow mapping.
---

# FDE Pain Analysis

## 核心目标

区分客户提出的表层方案和真实业务痛点，判断痛点影响的业务结果、关键角色和待验证假设。

## 使用时机

- 用户想知道客户原话背后的真实问题。
- 用户已有访谈记录或流程信息，需要识别痛点。
- 用户需要判断痛点影响效率、成本、增长、风控、客户体验还是标准化。

## 不使用时机

- 用户还没讲清业务背景：使用 `fde-intake`。
- 用户还没还原流程：使用 `fde-workflow-mapping`。
- 用户想判断 AI 是否适合：使用 `fde-ai-opportunity-assessment`。
- 用户想收敛交付范围：使用 `fde-mvp-scoping`。

## 强规则

- 客户提出的系统、工具、Agent 或自动化想法，先视为表层方案。
- 必须说明哪些是事实，哪些是假设。
- 必须指出谁真正受痛点影响，谁有动力推动，谁承担风险。
- 如果缺少流程和业务影响，不得断言真实痛点。

## 工作流程

1. 提取客户显性需求和表层方案。
2. 提取已知事实和待验证假设。
3. 从流程卡点中识别痛点候选。
4. 判断业务影响和关键角色。
5. 输出下一步验证问题。

## 输出格式

```markdown
## 表层需求
- ...

## 已知事实
- ...

## 待验证假设
- ...

## 真实痛点候选
| 痛点 | 影响环节 | 影响对象 | 业务影响 | 证据强度 |
| --- | --- | --- | --- | --- |

## 关键角色
- 最痛的人：
- 推动者：
- 决策者：
- 风险承担者：

## 下一步验证问题
1. ...
2. ...
3. ...
```

## 质量检查

- 是否区分了表层方案和真实痛点？
- 是否明确事实和假设？
- 是否定位到具体流程环节？
- 是否说明业务影响和关键角色？
- 是否避免了直接跳到 AI 方案？
