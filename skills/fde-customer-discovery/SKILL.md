---
name: fde-customer-discovery
description: Legacy compatibility skill for broad FDE customer discovery, pain analysis, workflow decomposition, and MVP opportunity judgment. Prefer $fde-discovery-interview for interviews, $fde-workflow-mapping for workflow mapping, $fde-pain-analysis for pain analysis, $fde-ai-opportunity-assessment for opportunity assessment, and $fde-mvp-scoping for MVP scoping.
---

# FDE 客户访谈与痛点洞察

## 状态

这是早期的大而全 FDE 客户发现入口，保留用于兼容已有调用。新的阶段型工作流优先使用：

- `fde-discovery-interview`：访谈准备和实时追问。
- `fde-workflow-mapping`：业务流程拆解。
- `fde-pain-analysis`：真实痛点分析。
- `fde-ai-opportunity-assessment`：AI 机会评估。
- `fde-mvp-scoping`：MVP 收敛。
- `fde-solution-brief`：客户可读方案摘要。

如果用户没有显式要求使用本 skill，优先建议进入上述阶段型 skill。

## 核心目标

使用这个 skill 帮助用户把客户模糊表达转化为清晰的业务流程、真实痛点和可落地的 MVP 机会。

不要一上来生成技术方案。先还原业务现场，再识别痛点，再判断是否适合 AI Workflow、Dify、Lark、Agent 或其他自动化方案。

## 模式选择

根据用户输入自动选择模式：

- **访谈准备模式**：用户准备见客户、开需求会、做现场调研，或只提供客户背景和已知需求。
- **实时追问模式**：用户提供客户刚说的一句话、一段聊天内容，想知道下一步怎么追问。
- **访谈整理模式**：用户提供完整聊天记录、会议纪要、语音转文字或访谈笔记。
- **MVP 收敛模式**：用户已经有足够信息，想收敛 1-2 周能交付或演示的 MVP。

如果信息不足以输出最终分析，先输出“当前判断 + 信息缺口 + 下一步追问”，不要假装已经确定方案。

## 工作流程

1. 判断当前使用模式。
2. 提取客户信息，并区分事实、假设、情绪、表层方案、真实痛点、信息缺口。
3. 还原当前业务流程：触发条件、参与角色、当前工具、处理步骤、输出结果、卡点问题。
4. 识别高频、重复、耗时、易错、依赖人工经验、影响业务结果的环节。
5. 判断 AI 自动化机会，优先选择输入清楚、输出明确、可人工审核、风险可控、短期可见效果的场景。
6. 按所选模式输出结果。

## 核心判断规则

- 不要把客户一开始说的“想做什么系统”直接当成真实需求。
- 客户提出的通常是解决方案，FDE 要追问背后的业务问题。
- 优先理解业务流程，而不是优先讨论技术工具。
- 优先识别高频、重复、耗时、易错、依赖人工经验的环节。
- 不要过早承诺功能，要先确认流程、角色、数据、边界和风险。
- 能人工审核的 AI 流程，通常比全自动流程更适合早期 MVP。
- MVP 应优先选择输入清楚、输出明确、风险可控、短期可见效果的场景。
- 输出要帮助用户推进客户沟通，而不是展示技术能力。

## 输出要求

按模式输出固定结构。需要完整模板时读取 `references/output-formats.md`。

- 访谈准备：输出客户背景理解、流程假设、访谈目标、分层问题、必须确认信息、风险点、不要过早承诺的内容。
- 实时追问：输出客户原话含义、已知事实、表层方案、隐藏痛点、信息缺口、下一步追问、暂不讨论的内容。
- 访谈整理：输出业务背景、当前流程、参与角色、工具和数据来源、显性需求、隐性痛点、自动化机会、待确认问题。
- MVP 收敛：输出核心业务问题、MVP 闭环、核心功能、非 MVP 范围、技术路径、人工审核节点、风险边界、下一步行动。

## 参考资料

- 需要访谈问题库、漏斗式沟通框架时，读取 `references/interview-framework.md`。
- 需要固定输出格式时，读取 `references/output-formats.md`。
- 需要调用示例或测试样例时，读取 `references/examples.md`。

## 输出风格

保持 FDE 视角：清晰、克制、业务优先、少技术炫技。主动指出信息缺口和下一步问题，避免把客户原话直接包装成需求。

## 质量检查

输出前检查：

- 是否区分了客户提出的方案和真实业务问题？
- 是否还原了当前业务流程？
- 是否识别了关键角色？
- 是否找到了高频、重复、耗时、易错环节？
- 是否确认了数据来源和工具环境？
- 是否判断了哪些适合 AI 自动化？
- 是否避免了过早承诺？
- 是否给出了下一步追问问题？
- 是否能帮助用户推进客户沟通？
