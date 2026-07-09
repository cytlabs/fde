---
name: fde-workflow-mapping
description: Use when turning customer descriptions, interview notes, meeting transcripts, or department scenarios into a structured business workflow before pain analysis, AI opportunity assessment, MVP scoping, or solution brief writing.
---

# FDE Workflow Mapping

## 核心目标

把客户零散口述还原成清晰业务流程，为后续痛点分析、AI 机会评估和 MVP 收敛提供输入。

## 使用时机

- 用户提供了业务流程描述、会议纪要、访谈记录或部门场景。
- 用户想知道某件事现在是怎么运转的。
- 用户准备进一步分析痛点或 AI 自动化机会。

## 不使用时机

- 用户还没提供任何流程背景：使用 `fde-intake`。
- 用户只是准备访谈问题：使用 `fde-discovery-interview`。
- 用户已有清楚流程，想判断 AI 可行性：使用 `fde-ai-opportunity-assessment`。

## 强规则

- 没有还原流程前，不得输出技术方案。
- 不得把客户提出的系统名称当成真实需求。
- 每个流程必须尽量补齐触发条件、角色、工具、步骤、输入、输出和卡点。
- 信息不足时，输出信息缺口和下一步追问，不得编造流程。

## 工作流程

1. 提取已知事实。
2. 区分事实、假设、表层方案和信息缺口。
3. 还原当前流程。
4. 标出高频、重复、耗时、易错、依赖经验的环节。
5. 输出待确认问题和建议进入的下一阶段。

## 输出格式

````markdown
## 当前流程

```text
触发条件 -> 参与角色 -> 当前工具 -> 处理步骤 -> 输入 -> 输出 -> 卡点问题
```

## 参与角色
- 发起者：
- 处理者：
- 审核者：
- 结果接收者：

## 工具和数据
- 工具：
- 数据来源：
- 数据形态：

## 流程卡点
- ...

## 高频重复或易错环节
- ...

## 信息缺口
1. ...

## 建议下一阶段
`fde-pain-analysis` / `fde-ai-opportunity-assessment`
````

## 质量检查

- 是否有清晰触发条件？
- 是否识别了参与角色？
- 是否列出当前工具和数据来源？
- 是否明确输入和输出？
- 是否指出卡点和信息缺口？
- 是否避免了过早给技术方案？
