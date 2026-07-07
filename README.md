# FDE Skills

FDE Skills 是一组面向 Forward Deployed Engineer / Field Deployment Engineer 的 Codex skills，用来辅助客户访谈、需求澄清、痛点洞察、业务流程拆解和 AI MVP 收敛。

这个项目的目标不是让 AI 一上来生成完整技术方案，而是帮助 FDE 在客户沟通中先把问题问清楚：客户真正想改善什么业务结果，当前流程如何运行，哪里高频、重复、耗时、易错，哪些环节适合先做成可人工审核的 MVP。

## 项目状态

当前处于早期版本，已经包含第一个可用 skill：`fde-customer-discovery`。

适合现在使用的场景：

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

### `fde-customer-discovery`

用于客户访谈、痛点洞察、业务流程拆解和 MVP 机会判断。

支持 4 种模式：

1. **访谈准备模式**：根据客户背景和已知需求，生成分层访谈问题、确认清单和风险点。
2. **实时追问模式**：分析客户刚说的一句话或一段话，判断表层方案、真实痛点和下一步追问。
3. **访谈整理模式**：把聊天记录、会议纪要或语音转文字整理成结构化 FDE 分析。
4. **MVP 收敛模式**：在信息足够时，收敛 1-2 周内可交付或可演示的 MVP 闭环。

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
5. 新开一个对话，使用 `$fde-customer-discovery`。

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
cp -R skills/fde-customer-discovery ~/.agents/skills/
```

重启 Codex 后，可以直接使用 `$fde-customer-discovery`。

## 快速开始

### 沟通前：生成访谈准备

```text
使用 $fde-customer-discovery。

客户是一家做海外达人营销的公司，目前他们说想用 AI 提高找达人、联系达人、客户需求对接、项目结项统计的效率。我准备和他们做一次线上沟通，请帮我生成访谈准备。
```

### 沟通中：分析客户原话

```text
使用 $fde-customer-discovery。

客户刚刚说：“我们现在主要问题是客户需求经常说不清楚，导致找来的达人不是客户想要的。”

请帮我分析这句话，并告诉我下一步应该追问什么。
```

### 沟通后：整理访谈记录

```text
使用 $fde-customer-discovery。

下面是今天的客户访谈记录，请帮我整理成 FDE 需求分析：
……
```

### 收敛 MVP

```text
使用 $fde-customer-discovery。

基于以上信息，请帮我收敛一个现场两周可以交付的 MVP，要求包含：业务目标、核心流程、功能范围、不做什么、人工审核节点、技术路径、风险边界和下一步确认问题。
```

## 仓库结构

```text
.
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   └── fde-customer-discovery/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
│           ├── examples.md
│           ├── interview-framework.md
│           └── output-formats.md
└── README.md
```

## 开发与校验

校验 marketplace JSON：

```bash
python3 -m json.tool .agents/plugins/marketplace.json
```

修改 skill 或 plugin manifest 后，建议在本地 Codex 环境中重新安装 marketplace，并用 `/plugins` 确认 `FDE Skills` 可以被发现和安装。然后新开一个对话，显式调用 `$fde-customer-discovery` 跑一遍“沟通前”“沟通中”“沟通后”三个示例。

如果你的 Codex 环境提供 skill/plugin 校验脚本，也建议同时校验：

- `skills/fde-customer-discovery` 是合法 skill。
- 仓库根目录是合法 plugin。
- `.agents/plugins/marketplace.json` 可以解析，并且指向仓库根目录 `./`。

## 路线图

- 增加 `fde-mvp-scoping`：专门做 MVP 范围、交付阶段和验收标准收敛。
- 增加 `fde-workflow-analysis`：专门把复杂业务口述拆成流程图、角色泳道和系统边界。
- 增加 `fde-ai-opportunity-assessment`：专门评估业务场景是否适合 AI Workflow、Agent、RPA 或传统系统。
- 增加 `fde-solution-brief`：把访谈结果转成客户可读的初步方案文档。
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
- 不过早承诺功能和交付范围。
