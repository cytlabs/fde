---
name: fde-discovery-interview
description: Prepare or conduct an FDE customer discovery interview. Use preparation mode to generate a layered interview plan; use live mode when the user provides a customer's latest statement and asks what to ask next. Do not use to conclude the real pain, map a complete supplied workflow, assess AI feasibility, or scope an MVP.
---

# FDE Discovery Interview

## 核心目标

帮助 FDE 做访谈准备和实时追问，把客户模糊表达拆成可验证的问题。这个 skill 只负责访谈阶段，不负责完整流程建模、AI 机会排序、MVP 收敛或方案文档。

## 使用时机

- 用户准备见客户、开需求会、做现场调研。
- 用户提供客户背景，希望生成访谈问题。
- 用户提供客户刚说的一句话，想知道下一步怎么追问。
- 用户需要识别当前信息缺口。
- 用户需要一线员工现场访谈话术、访谈检查清单或真实材料收集指引时，读取 `references/frontline-employee-interview-playbook.md`。

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
- 访谈前模式必须使用完整模板；未知内容写 `待确认`，不得自行省略栏目。
- 实时模式优先简洁：必须给出一个主问题和提问原因；仅在存在明显分支时给出最多两个备选问题。

## 工作流程

1. 判断用户是在访谈前准备，还是实时追问。
2. 区分已知事实、客户假设、表层方案、信息缺口。
3. 设计分层问题：业务目标、当前流程、角色分工、痛点、数据工具、MVP 可能性。
4. 访谈前输出完整问题树；实时追问只输出一个主问题和最多两个备选问题。
5. 指出暂时不要承诺的内容。

## 参考材料

- `references/frontline-employee-interview-playbook.md`：一线员工现场访谈话术、真实材料收集方法、结束前六件事检查清单和访谈记录模板。

## 输出格式：访谈前准备

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

## 交接记录
- 已确认事实：...
- 当前假设：...
- 可用证据：...
- 信息缺口：...
```

## 输出格式：实时追问

```markdown
## 当前判断
- 客户刚确认了什么：...
- 仍然只是推测什么：...

## 下一问
**问题：** ...

**为什么现在问：** ...

## 备选追问
1. ...（仅在有价值时提供）
2. ...（仅在有价值时提供）

## 本轮要记录
- 事实：...
- 证据：...
- 新增信息缺口：...

## 暂时不要下的结论
- ...
```

## 质量检查

- 是否生成了能推进访谈的问题？
- 是否避免把客户表层方案当需求？
- 是否按层次追问，而不是泛泛问痛点？
- 是否指出了不能过早承诺的内容？
- 实时模式是否只给出一个最高优先级主问题，而不是整套问题清单？
