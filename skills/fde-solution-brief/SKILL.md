---
name: fde-solution-brief
description: Turn confirmed FDE discovery and MVP outputs into a customer-readable solution brief, proposal summary, phased delivery outline, risk boundary, and next-step document. Use only when the business problem, recommended first-stage scope, evidence, non-goals, review points, and validation approach are already available. Do not use to fill discovery gaps or invent an MVP.
---

# FDE Solution Brief

## 核心目标

把已确认的客户背景、业务问题、流程、痛点、AI 机会和 MVP 范围，整理成客户可读的方案摘要或沟通材料。

## 使用时机

- 用户已有访谈、流程、痛点、AI 机会或 MVP 信息。
- 用户想生成客户可读的初步方案文档。
- 用户需要向客户解释第一阶段做什么、不做什么、为什么。

## 不使用时机

- 信息还不完整，需要先访谈：使用 `fde-discovery-interview`。
- 流程还不清楚：使用 `fde-workflow-mapping`。
- 痛点或 AI 机会还未判断：使用 `fde-pain-analysis` 或 `fde-ai-opportunity-assessment`。
- MVP 范围还未确定：使用 `fde-mvp-scoping`。

## 强规则

- 不得新增未经确认的承诺。
- 不要过度技术化，优先讲业务问题、闭环和预期验证方式。
- 必须明确人工审核、风险边界和后续待确认事项。
- 如果信息不足，先列缺口，不要包装成完整 proposal。

## 工作流程

1. 提取已确认信息。
2. 将事实、假设和待确认事项分开，假设不得写成承诺。
3. 组织客户可读叙事：背景、问题、推荐试点、MVP 闭环、阶段计划。
4. 明确不做范围、风险边界和客户需要确认的问题。
5. 输出简洁、可发送的材料。

## 输出格式

```markdown
## 初步方案摘要

...

## 当前业务问题
- ...

## 推荐第一阶段 MVP
- 场景：
- 推荐原因：
- 输入：
- 输出：
- 人工审核：

## 交付阶段

### 第 1 阶段
- ...

### 后续阶段
- ...

## 暂不包含的范围
- ...

## 风险边界
- ...

## 待客户确认
1. ...
2. ...
3. ...

## 依据与假设
- 已确认依据：...
- 尚待验证假设：...
```

## 质量检查

- 是否只使用已确认信息？
- 是否客户可读，而不是技术炫技？
- 是否明确第一阶段和后续阶段？
- 是否写清楚不做什么和风险边界？
