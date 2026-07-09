---
name: fde-discovery-interview
description: Use when preparing or conducting an FDE customer discovery interview, generating layered interview questions, analyzing a customer's latest statement, deciding what to ask next, or identifying information gaps before workflow mapping or solution scoping.
---

# FDE Discovery Interview

## 核心目标

帮助 FDE 做访谈准备和实时追问，把客户模糊表达拆成可验证的问题。这个 skill 只负责访谈阶段，不负责完整流程建模、AI 机会排序、MVP 收敛或方案文档。

## 使用时机

- 用户准备见客户、开需求会、做现场调研。
- 用户提供客户背景，希望生成访谈问题。
- 用户提供客户刚说的一句话，想知道下一步怎么追问。
- 用户需要识别当前信息缺口。

## 不使用时机

- 用户已有完整流程材料，需要还原流程：使用 `fde-workflow-mapping`。
- 用户想判断真实痛点：使用 `fde-pain-analysis`。
- 用户想判断 AI 是否适合：使用 `fde-ai-opportunity-assessment`。
- 用户想收敛 MVP：使用 `fde-mvp-scoping`。

## 强规则

- 客户提出的方案不是需求本身，必须追问背后的业务问题。
- 不要一上来讨论工具选型。
- 问题必须从业务目标到流程、角色、痛点、数据、风险逐层推进。
- 信息不足时，输出下一步追问，不要假装确定结论。

## 工作流程

1. 判断用户是在访谈前准备，还是实时追问。
2. 区分已知事实、客户假设、表层方案、信息缺口。
3. 设计分层问题：业务目标、当前流程、角色分工、痛点、数据工具、MVP 可能性。
4. 指出暂时不要承诺的内容。

## 输出格式

```markdown
## 当前访谈判断

...

## 已知事实
- ...

## 信息缺口
- ...

## 分层追问

### 业务目标
- ...

### 当前流程
- ...

### 角色分工
- ...

### 痛点和影响
- ...

### 数据与工具
- ...

## 暂时不要承诺
- ...
```

## 质量检查

- 是否生成了能推进访谈的问题？
- 是否避免把客户表层方案当需求？
- 是否按层次追问，而不是泛泛问痛点？
- 是否指出了不能过早承诺的内容？
