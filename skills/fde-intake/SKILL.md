---
name: fde-intake
description: Use when collecting customer-side context before an FDE conversation, especially when a business user has vague AI transformation goals and needs to prepare enterprise background, business objectives, current problems, candidate workflows, data/tool context, and questions for an FDE.
---

# FDE Intake

## 核心目标

帮助客户在和 FDE、AI 顾问或实施方沟通前，整理一份前置沟通包。这个 skill 只负责前置信息收集，不做深度流程建模、最终痛点判断、AI 方案承诺或 MVP 范围收敛。

## 使用时机

- 用户说想做 AI 转型、AI 提效、业务诊断，但还没有明确场景。
- 用户准备和 FDE 沟通，希望提前整理材料。
- 用户只能描述企业背景和模糊问题，还不能给出完整流程。

## 不使用时机

- 用户已经提供了具体流程，需要拆步骤：使用 `fde-workflow-mapping`。
- 用户正在准备访谈问题或追问客户：使用 `fde-discovery-interview`。
- 用户已经有候选场景，想判断 AI 可行性：使用 `fde-ai-opportunity-assessment`。
- 用户想收敛交付范围：使用 `fde-mvp-scoping`。

## 强规则

- 不要把“想用 AI”当作需求本身。
- 不要输出最终技术方案。
- 不要承诺自动化效果。
- 信息不足时，优先输出信息缺口和补充问题。

## 工作流程

1. 提取企业背景：行业、规模、业务模式、部门。
2. 提取业务目标：降本、提效、增长、风控、标准化、客户体验。
3. 识别客户已知问题和候选流程。
4. 盘点当前工具、数据位置、历史样例和权限情况。
5. 输出给 FDE 的前置沟通包和待确认问题。

## 输出格式

```markdown
## 给 FDE 的前置沟通包

### 企业背景
- 行业：
- 规模：
- 主要业务：

### 当前目标
- ...

### 已知问题
- ...

### 候选业务流程
- ...

### 当前工具和数据
- 工具：
- 数据位置：
- 历史样例：
- 权限/API 情况：

### 和 FDE 沟通时要确认的问题
1. ...
2. ...
3. ...
```

## 质量检查

- 是否让客户更容易和 FDE 沟通？
- 是否避免了过早给方案？
- 是否明确了哪些信息还缺失？
- 是否把输出控制在前置沟通包，而不是完整诊断？
