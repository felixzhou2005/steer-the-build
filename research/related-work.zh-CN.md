# 相关工作

> 状态：v0.1 的初始公开资料扫描。这是一份持续维护的比较，不是穷尽性的文献综述。

Steer the Build 与多个正在发展的方向存在交集：规格驱动开发、Agent Skill、AI 开发模式、生产级 Agent 控制框架、自动化测试、可观察性、安全开发和交付效能。下表明确重叠点与边界。

## 相邻项目与实践

| 资料 | 主要关注点 | 与本项目的交集 | 本项目的差异或吸收的经验 |
|---|---|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) | AI 编码中的规格驱动开发工具包 | 把 specification、plan、tasks 和 implementation 分开 | 本项目进一步覆盖 AI 原生 Review、运行证据、逆向诊断、分层 Skill、发布治理和跨领域案例 |
| [Addy Osmani 的 Agent Skills](https://github.com/addyosmani/agent-skills) | 设计、代码质量、测试、性能、安全和工作流 Skill | 把 Skill 作为持续复用的工程指令 | 本项目把 Skill 视为受治理的学习系统：缺陷 → 规则 → 回归测试 → Skill 版本 → 历史验证 |
| [AI Development Patterns](https://github.com/PaulDuvall/ai-development-patterns) | AI 软件交付的模式和反模式 | 可重复的工程实践和质量控制 | 本项目采用四平面控制系统、证据授权、双语模板和真实案例骨架 |
| [Reins](https://github.com/WellDunDun/reins) | 引导 AI 编码代理生成可维护软件的控制框架 | 对 Agent 设置明确约束和控制 | 本项目主要是工具无关、模型无关的方法论与现场手册，而不是单一运行框架 |
| [Thoughtworks：Vibe Coding 能否产生生产级软件？](https://thoughtworks.medium.com/can-vibe-coding-produce-production-grade-software-75130f25b63d) | 比较自由式 Prompt 与有意识工程约束的实验 | 人的掌舵、模块化、可测试性和可维护性 | 本项目增加完整生命周期、大代码量下的 AI 原生 Review、AI 可读可观察性和 Skill 反馈闭环 |

## 证据与验证基础

| 资料 | 在本项目中的作用 |
|---|---|
| [pytest](https://docs.pytest.org/) | Python 单元、集成、性质和回归测试的代表性基础 |
| [Playwright](https://playwright.dev/docs/intro) | 浏览器关键流程和端到端证据 |
| [Maestro](https://docs.maestro.dev/) | Mobile UI 流程自动化和 Agent 驱动执行 |
| [OpenTelemetry 可观察性入门](https://opentelemetry.io/docs/concepts/observability-primer/) | 日志、指标、Trace、上下文传播和系统行为的共同语言 |
| [DORA Metrics](https://dora.dev/guides/dora-metrics/) | 防止把“生成代码行数”当成唯一生产力指标 |
| [NIST 安全软件开发框架](https://csrc.nist.gov/pubs/sp/800/218/final) | 安全开发职责和实践的基线 |

## Agent 运维与安全

| 资料 | 相关性 |
|---|---|
| [OpenClaw 安全指南](https://docs.openclaw.ai/gateway/security) | Gateway、可信操作者、凭据、隔离和部署边界 |
| [OpenClaw CLI 安全](https://docs.openclaw.ai/cli/security) | 强调把 Skill 和 Plugin 当成可执行代码，并使用明确权限 |
| [OpenClaw Skills 文档](https://docs.openclaw.ai/tools/skills) | Skill 的组织和调用方式参考 |

## 明确不做的主张

- 不主张只要有文档就一定正确。
- 不主张 AI Review 可以取消人的最终责任。
- 不主张高风险决策不再需要人工审查。
- 不主张某一个模型或工具永远最好。
- 不主张缺少软件工程经验的人可以自然控制所有复杂系统。
- 不主张所有项目都应追求最大自治。

## 如何补充相关工作

有效的补充应回答四个问题：

1. 资料解决了什么问题？
2. 与 Steer the Build 的哪条原则重叠？
3. 有什么实质差异？
4. 本项目应当因此学习或修改什么？

可提交带 `related-work` 标签的 Issue，或同时修改中英文页面的 Pull Request。
