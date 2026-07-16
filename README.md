# FDE Skills

FDE Skills 是一组面向企业客户和 Forward Deployed Engineer / Field Deployment Engineer 的阶段型 Codex skills，用来辅助 AI 转型前置信息收集、客户访谈、流程拆解、痛点分析、AI 机会评估、MVP 收敛和方案表达。

这个项目的目标不是让 AI 一上来生成完整技术方案，而是把 FDE 工作流拆成多个可组合阶段：先整理背景，再访谈追问，再还原流程，再识别痛点，再评估 AI 机会，最后才收敛 MVP 和表达方案。

## 项目状态

各阶段通过“事实、假设、证据、信息缺口”交接，仓库内提供路由和行为 eval 语料。

适合现在使用的场景：

- 企业客户在和 FDE 沟通前做 AI 转型前置诊断
- 盘点现有业务流程，识别可能适合 AI 提效的环节
- 整理可发给 FDE 的前置沟通包
- 准备客户访谈问题
- 分析客户原话，判断下一步怎么追问
- 整理客户访谈记录
- 识别显性需求背后的真实业务痛点
- 判断 AI Workflow / Dify / Lark / Agent 是否适合落地
- 收敛 1-2 周内可演示的 MVP 闭环

暂时不适合直接用于：

- 自动生成完整售前方案
- 替代 FDE 做最终业务判断
- 替代法律、财务、人事、安全等高风险决策
- 在没有人工审核的情况下直接承诺全自动交付

## 当前包含的 Skill

### 推荐阶段型 Skills

| Skill | 阶段 | 产物 |
| --- | --- | --- |
| `fde-engagement-router` | 路由 | 当前阶段判断和推荐 skill |
| `fde-intake` | 前置收集 | 客户前置沟通包 |
| `fde-discovery-interview` | 访谈 | 访谈问题、实时追问、信息缺口 |
| `fde-workflow-mapping` | 流程拆解 | 流程、角色、工具、输入输出、卡点 |
| `fde-pain-analysis` | 痛点分析 | 表层需求、真实痛点、业务影响 |
| `fde-ai-opportunity-assessment` | AI 机会评估 | 候选场景适合度和优先级 |
| `fde-mvp-scoping` | MVP 收敛 | MVP 闭环、边界、人工审核节点 |
| `fde-solution-brief` | 方案表达 | 客户可读方案摘要 |

## 安装

### 通过 GitHub 安装插件

把本仓库作为 Codex plugin marketplace 添加：

```bash
codex plugin marketplace add owner/repo
```

把 `owner/repo` 替换成你的 GitHub 仓库，例如：

```bash
codex plugin marketplace add yourname/fde
```

固定分支：

```bash
codex plugin marketplace add yourname/fde --ref main
```

完整 Git URL：

```bash
codex plugin marketplace add https://github.com/yourname/fde.git
```

添加 marketplace 后：

1. 重启 Codex。
2. 在 Codex CLI 中打开 `/plugins`。
3. 切换到 `FDE Skills` marketplace。
4. 安装 `FDE Skills` 插件。
5. 新开一个对话，优先使用 `$fde-engagement-router` 判断阶段，或直接调用具体阶段 skill。

### 本地安装

如果还没有推到 GitHub，可以本地安装：

```bash
git clone https://github.com/yourname/fde.git
codex plugin marketplace add ./fde
```

把 `https://github.com/yourname/fde.git` 替换成你的仓库地址。

然后重启 Codex，在 `/plugins` 中安装 `FDE Skills`。

### 手动安装单个 skill

如果你的 Codex 环境暂时不使用插件，可以只复制 skill：

```bash
cd fde
mkdir -p ~/.agents/skills
cp -R skills/fde-engagement-router ~/.agents/skills/
cp -R skills/fde-intake ~/.agents/skills/
cp -R skills/fde-discovery-interview ~/.agents/skills/
cp -R skills/fde-workflow-mapping ~/.agents/skills/
cp -R skills/fde-pain-analysis ~/.agents/skills/
cp -R skills/fde-ai-opportunity-assessment ~/.agents/skills/
cp -R skills/fde-mvp-scoping ~/.agents/skills/
cp -R skills/fde-solution-brief ~/.agents/skills/
```

重启 Codex 后，可以直接使用 `$fde-engagement-router` 或任一阶段型 skill。

## 快速开始

### 判断当前阶段

```text
使用 $fde-engagement-router。

客户说他们想做一个销售 Agent，但现在只知道销售团队很忙。我应该先进入哪个 FDE 阶段？
```

### 客户侧：生成 FDE 前置沟通包

```text
使用 $fde-intake。

我们是一家做 B2B 销售的公司，销售团队每天要写跟进记录、整理客户需求、准备方案，也想看看客服和交付环节有没有 AI 提效空间。请帮我整理一份和 FDE 沟通前的业务材料。
```

### FDE 侧：第一次见老板做商机判断

```text
使用 $fde-intake。

我明天第一次见一家制造业公司的老板，对方说想了解 AI 能不能帮公司提效。请按老板首访问题帮我准备 qualification 问题，并告诉我每个问题背后要判断什么。
```

### 沟通前：生成访谈准备

```text
使用 $fde-discovery-interview。

客户是一家做海外达人营销的公司，目前他们说想用 AI 提高找达人、联系达人、客户需求对接、项目结项统计的效率。我准备和他们做一次线上沟通，请帮我生成访谈准备。
```

### 沟通中：分析客户原话

```text
使用 $fde-discovery-interview。

客户刚刚说：“我们现在主要问题是客户需求经常说不清楚，导致找来的达人不是客户想要的。”

请帮我分析这句话，并告诉我下一步应该追问什么。
```

### 沟通后：整理访谈记录

```text
使用 $fde-workflow-mapping。

下面是今天的客户访谈记录，请帮我整理成业务流程、角色、工具、输入输出和卡点：
……
```

### 收敛 MVP

```text
使用 $fde-mvp-scoping。

基于以上信息，请帮我收敛一个现场两周可以交付的 MVP，要求包含：业务目标、核心流程、功能范围、不做什么、人工审核节点、技术路径、风险边界和下一步确认问题。
```

MVP 验收必须同时给出当前基线、目标、测试样本、测量方式和验收责任人；缺少这些信息时先列缺口，不编造百分比目标。

## 仓库结构

```text
.
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── evals/
│   └── cases.json
├── scripts/
│   └── validate_repo.py
├── skills/
│   ├── fde-ai-opportunity-assessment/
│   ├── fde-discovery-interview/
│   ├── fde-engagement-router/
│   ├── fde-intake/
│   ├── fde-mvp-scoping/
│   ├── fde-pain-analysis/
│   ├── fde-solution-brief/
│   └── fde-workflow-mapping/
└── README.md
```

## 开发与校验

校验 marketplace JSON：

```bash
python3 -m json.tool .agents/plugins/marketplace.json
```

一次性校验 plugin manifest、skill 结构和 eval 语料：

```bash
python3 scripts/validate_repo.py
```

`evals/cases.json` 定义预期 skill、模式、必须覆盖内容和禁止行为。当前脚本校验 eval 语料的结构与覆盖范围；修改行为契约后，还应在新对话中用这些 prompt 做 forward test。

修改 skill 或 plugin manifest 后，建议在本地 Codex 环境中重新安装 marketplace，并用 `/plugins` 确认 `FDE Skills` 可以被发现和安装。然后新开一个对话，优先显式调用 `$fde-engagement-router` 跑一遍阶段判断，再分别调用 `$fde-intake`、`$fde-discovery-interview`、`$fde-workflow-mapping` 和 `$fde-mvp-scoping` 跑通主路径。

如果你的 Codex 环境提供 skill/plugin 校验脚本，也建议同时校验：

- `skills/*` 下每个 skill 都是合法 skill。
- 仓库根目录是合法 plugin。
- `.agents/plugins/marketplace.json` 可以解析，并且指向仓库根目录 `./`。

## 路线图

- 接入自动化 model eval runner，基于现有 `evals/cases.json` 检查真实输出。
- 增加共享方法论 references：沉淀 FDE 原则、MVP 选择规则、风险边界和常见反模式。
- 增加行业案例 references：达人营销、电商运营、销售 CRM、客服、财务、人事等。
- 增加可复制的交付模板：调研纪要、MVP proposal、风险评估表、客户确认清单。
- 后续按需接入 MCP，例如读取飞书、Notion、GitHub、CRM、数据库或内部文档。

## 贡献

欢迎提交 issue 和 pull request，尤其是以下方向：

- 更真实的 FDE 访谈场景
- 更稳定的追问框架
- 不同行业的痛点识别案例
- 更好的 MVP 收敛模板
- Codex plugin / skill 安装体验改进

贡献时请保持每个 skill 聚焦一个任务，不要把多个独立能力塞进同一个 `SKILL.md`。详细案例、模板和问题库优先放到 `references/`，让主 skill 保持轻量。

## 许可证

本项目使用 MIT License。你可以自由使用、复制、修改、分发和商用，但需要保留原始版权声明和许可证文本。

## 核心原则

- 先还原业务，再谈技术。
- 先识别真实痛点，再讨论解决方案。
- 先做可人工审核的 MVP，再考虑全自动。
- 不把客户原话直接当需求。
- 事实、假设和证据分开记录，阶段之间传递信息缺口。
- 不过早承诺功能和交付范围。
