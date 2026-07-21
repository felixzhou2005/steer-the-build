## 40. GitHub 与 LinkedIn 上是否已有相似内容：有明显重叠，但仍有差异化空间
公开可检索的 GitHub 和 LinkedIn 内容已经广泛讨论规格驱动开发、先规划后实现、Agent Skill、自动化测试、可观察性、架构重要性和人类控制。因此，不能把项目定位为“AI 编程也需要需求、架构和测试”——这个观点本身已经不新。检索结果并非穷尽，尤其 LinkedIn 的公开索引有限，但足以说明主要重叠面。

| **相近内容**                          | **已有内容的重点**                                     | **与本项目的重叠**               | **本项目应怎样避开重复**                                 |
|---------------------------------------|--------------------------------------------------------|----------------------------------|----------------------------------------------------------|
| GitHub Spec Kit / Spec-driven 项目    | 规格、计划、任务、实现、项目 Constitution 和可追踪流程 | 完整需求、先方案后代码、质量约束 | 不再造一个通用 CLI；重点写跨项目实证、失败和人的控制边界 |
| OpenSpec / 其他 SDD 工作流            | 把规格作为唯一真相、管理变更和 Agent 执行              | 文档控制面、变更可追踪           | 强调思考过程文字化、AI 原生 Review 和结果逆向诊断        |
| Agent Skills / Quality Playbook       | 把高级工程师工作流、质量门和最佳实践打包为 Skill       | Skill 沉淀和一致性               | 提出分层、项目具体化、历史失败验证、冲突与退役治理       |
| AI development patterns / playbooks   | 按生命周期归纳规格、测试、可观察性和运维模式           | 方法论和模式化表达               | 提供真实跨域实践、明确标注为个人估算的规模经验和后续证据计划 |
| LinkedIn 的架构 / 测试 / 可观察性文章 | AI 速度需要更多架构、测试、CI/CD、安全和 Telemetry     | 基本工程原则高度一致             | 用连续案例、失败证据、工具工件和人的角色变化形成个人主线 |
| Vibe coding 反思与教程                | 从快速原型到工程化、上下文、提示和质量门               | 反对直接让 AI 开干               | 不做入门教程；面向复杂系统和已有工程经验的人             |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>建议的独特定位</strong></p>
<p><strong>这不是提示词合集、AI 工具评测、Spec CLI 或“全自动软件公司”。它是一套来自业务、Mobile、IoT、语音、ML 和云部署实践的“人类控制、AI 执行、证据驱动”方法，重点解决代码规模暴增后的 Review、测试、可观察性、逆向诊断、Skill 复利和工程责任。</strong></p></th>
</tr>
</thead>

</table>

### 40.1 最值得长期占据的六个差异化主题
> **•** 跨项目实证：同一方法在业务、移动、硬件、语音、算法和云服务中的变化，而不是只讲 Web CRUD。
>
> **•** 完全委托编码之后怎样控制：不以“人必须逐行读完”为前提，建立 AI 原生 Review 和证据体系。
>
> **•** 从结果逆向到根因：展示复杂算法和跨层系统如何通过第一个异常点定位，而不是让 Agent 连续随机修补。
>
> **•** Skill 的工程化复利：分层、项目化、测试、版本、冲突、退役和从缺陷回写，而不是分享一堆 prompt。
>
> **•** 人的不可替代价值：审美、架构、算法、技术选型、性能建模和最终责任的具体边界。
>
> **•** 软件经济与职业变化：低成本个性化如何扩大软件市场，以及高级工程师为什么会成为更强的放大器。

## 41. GitHub：把它做成中英文、可贡献的长期主项目
GitHub 应当是完整内容、模板、案例、Skill 和讨论的“规范源”；LinkedIn 用来传播单一观点和真实片段，并把有兴趣的人引导到 GitHub。不要把两边都写成同一篇超长文章。

### 41.1 推荐名称与一句话定位
中文主标题：人类控制的 AI 软件工程：从意图到证据

英文主标题：Human-in-Control AI Software Engineering: From Intent to Evidence

仓库名候选：human-in-control-ai-engineering；intent-to-evidence；controlled-ai-software-engineering。发布前仍应在 GitHub 实时检查名称、组织名和商标冲突。相比泛化的“AI-native engineering”，这些名称更能承载你的控制边界和证据主线。

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>一句话定位 / Positioning</strong></p>
<p>中文：一套来自跨类型真实项目的 AI 软件工程方法：人定义问题、架构、算法、审美、风险和证据，AI 执行研究、编码、Review、测试、诊断与开发运维。<br />
English: A practitioner-led method for building real software with humans controlling intent, architecture, algorithms, taste, risk and evidence, while AI executes research, coding, review, testing, diagnosis and development operations.</p></th>
</tr>
</thead>

</table>

### 41.2 双语结构：不要把中英文逐段并排塞进同一文件
> **•** README.md 以英文为默认入口，顶部提供“简体中文”切换；README.zh-CN.md 是中文入口。
>
> **•** 正文采用 docs/en/ 与 docs/zh-CN/ 同名文件；案例和模板保持一一对应。
>
> **•** 确定一个规范源语言。你可以先以中文为规范源，英文文件记录 source commit / translation status，避免两套内容悄悄分叉。
>
> **•** 不要机械直译 LinkedIn 帖子；英文版应重新组织 Hook、例子和文化语境，但事实、指标和方法保持一致。

| **建议目录**                                          | **用途**                                                                                                    |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| README.md / README.zh-CN.md                           | 项目定位、核心原则、快速导航、案例入口和贡献方式                                                            |
| docs/en/ 与 docs/zh-CN/                               | manifesto、method、ai-native-review、testing、observability、skills、human-role、devops、software-economics |
| case-studies/                                         | home-valuation、ios-app、iot-control、ai-receptionist、voice-translation、openclaw-service 等真实案例       |
| skills/base/                                          | 简单优先、先方案后实现、证据完成、禁止范围扩张等 L0 Skill                                                   |
| skills/domain/ 与 skills/project/                     | SQL、iOS、ML、IoT、语音、DevOps 以及项目具体约束                                                            |
| templates/                                            | 需求、架构、实现计划、测试计划、Review、可观察性、事故与案例模板                                            |
| research/related-work.md                              | 持续维护相近项目、文章、差异矩阵与本项目借鉴边界                                                            |
| CONTRIBUTING / CODE_OF_CONDUCT / GOVERNANCE / ROADMAP | 贡献质量门、社区行为、维护决策和版本计划                                                                    |
| LICENSE 与内容许可说明                                | 明确文字、模板、Skill 和代码的使用、修改与分发权利                                                          |

### 41.3 GitHub v0.1 不要铺得太大
第一版只发布边界一致的最小完整集：中英文 README、完整方法论、核心生命周期、AI 原生 Review、测试与可观察性、Skill 分层方法、工程模板、相关工作、贡献指南和许可证。需要真实证据的案例和经过验证的实际 Skill 留在本地完善，达到公开标准后再进入后续版本。

## 42. GitHub 贡献机制：让别人补充经验，而不是堆积观点
开放贡献时，最容易出现的是未经验证的“我觉得”、重复原则和通用 prompt。应把贡献分成案例、反例、Skill、模板和相关研究五类，每类都有证据要求。GitHub Discussions 适合开放式方向讨论、问答和案例交流；Issue 用于范围明确的缺陷和任务；Pull Request 用于可审查的内容变更。

| **贡献类型** | **最低证据标准**                                                 |
|--------------|------------------------------------------------------------------|
| 案例         | 背景、约束、人的决定、AI 执行、失败、证据、结果、Skill、隐私处理 |
| 反例 / 事故  | 可复现症状、影响、日志/测试、根因、修复、为什么现有规则未能阻止  |
| Skill        | 层级、触发、不触发、规则、正反例、历史失败验证和兼容范围         |
| 模板         | 解决什么重复问题、至少一个真实使用示例、与现有模板的差异         |
| 相关工作     | 准确摘要、重叠点、差异点、可借鉴内容，禁止只贴链接               |
| 翻译         | 对应源 commit、术语表、内容完整性检查和语言自然度审查            |

> **•** Discussions 分类建议：案例与反例、Skill 提案、方法争议、工具与证据、翻译、相关工作。
>
> **•** 所有案例必须允许匿名化；禁止上传客户代码、密钥、原始通话、个人数据或无授权的数据集。
>
> **•** 许可证必须在首次公开时明确。若文字与可执行 Skill 采用不同许可证，应在目录和文件头清楚标注；具体选择涉及法律含义时应再做专业确认。

## 43. LinkedIn：先做十篇方法系列，再穿插项目案例
LinkedIn 更适合一个帖子只讲一个有冲突感的结论，并用一个真实项目片段证明。建议先用十篇建立完整主线，再进入案例季。中文和英文可以错开发布；每篇以一种语言为主，末尾给另一语言的简短摘要和 GitHub 双语入口，比同一帖子中放两篇全文更易读。

| **序号** | **建议标题 / Hook**                                     | **核心案例或证据**                     |
|----------|---------------------------------------------------------|----------------------------------------|
| 1        | 个人估算 AI 写了 30 万行代码：但工程责任一行也没有少     | 方法总论、人的工作上移、效率与边界     |
| 2        | 为什么 AI 编程必须从完整需求文档开始                    | 一次从需求直接实现导致的返工           |
| 3        | 不要让 AI 直接开干：先审方案，再让它实现                | 方案审核如何避免结构失控               |
| 4        | 代码太多以后，Review 本身必须 AI 原生化                 | 四层 Review、人的风险门和抽样审计      |
| 5        | 测试才是大规模 AI 代码的主要信任机制                    | pytest、Playwright、Maestro 与失败工件 |
| 6        | Skill 不是 prompt 集合，而是工程记忆                    | 分层 Skill、Figma 复刻、缺陷到规则     |
| 7        | 日志是给人看的，也是给 AI 检索的                        | 结构化日志如何快速定位跨层问题         |
| 8        | 人的价值没有消失：审美、架构、算法和判断                | UI 灵魂、NoSQL/架构/模型选择           |
| 9        | 为什么让 AI 一直重试通常会走进死胡同                    | 复杂算法从结果拆分到第一个异常点       |
| 10       | AI 降低开发成本后，个性化软件会从例外变成默认           | 客户特定系统、长尾市场与维护风险       |

### 43.1 每篇 LinkedIn 帖子的固定骨架
> **1 开头冲突**：用一句反常识判断或真实数字，不先讲背景。
>
> **2 具体场景**：说明是哪类项目、什么约束，不泄露客户信息。
>
> **3 失败或代价**：展示为什么常见做法不够，而不是只呈现成功。
>
> **4 你的方法**：给出三到五个可执行步骤或一张简图。
>
> **5 证据**：测试、日志、指标、周期或前后对比；没有数据时明确是个人观察。
>
> **6 边界**：指出什么场景不适用、仍有什么风险。
>
> **7 讨论问题**：邀请读者贡献自己的反例或案例，而不是泛泛地问“你怎么看”。
>
> **8 GitHub 入口**：指向对应章节或案例，不只指向仓库首页。

### 43.2 第二阶段：项目案例系列
十篇方法系列之后，每个深案例可以拆成两到三篇：第一篇讲人的关键设计，第二篇讲失败与逆向诊断，第三篇讲测试、日志和 Skill。这样项目不只是“作品展示”，而会持续反向证明方法论。

## 44. 推荐发布顺序：先建立可信的最小闭环
| **阶段**          | **发布内容**                                                         | **目标**                             |
|-------------------|----------------------------------------------------------------------|--------------------------------------|
| 0\. 准备          | 清理可公开材料、确认维护者身份、许可证、统计边界和术语表             | 避免仓促公开造成隐私和可信度问题     |
| 1\. GitHub v0.1   | 双语 README、核心方法、模板、相关工作、治理和贡献指南                | 建立稳定、可引用的方法论规范源       |
| 2\. 证据版本      | 逐个补充深度案例、验证后的实际 Skill 和脱敏证据                     | 让案例和 Skill 真正支撑方法主张      |
| 3\. 社区吸收      | 用 Discussions 收集案例和争议，Issue 管理明确改进，PR 接受证据化贡献 | 把外部经验纳入结构，而不稀释主线     |
| 4\. 版本复盘      | 按真实新增案例、Skill 和反例发布 v0.2 / v0.3 变更说明                | 让方法由证据演化，不追求无休止扩写   |

---

## 46. GitHub README 双语开场草案
### 中文草案
这不是一个提示词合集，也不是一个让 AI 自主完成软件的框架。它记录一种来自真实业务、Mobile、IoT、语音、机器学习和云部署项目的工程方法：人控制问题、需求、架构、算法、审美、风险与证据，AI 执行研究、方案、编码、Review、测试、诊断和开发运维。核心目标不是生成更多代码，而是在代码规模快速增长后，仍然能够知道系统为什么这样设计、怎样证明它正确、出现偏差时从哪里开始逆向分析，以及如何把每次经验固化成可复用 Skill。

### English draft
This is not a prompt collection or a framework for fully autonomous software delivery. It documents a practitioner-led method developed across real business, mobile, IoT, voice, machine-learning and cloud-deployment projects: humans control the problem, requirements, architecture, algorithms, product taste, risk and evidence; AI executes research, planning, coding, review, testing, diagnosis and development operations. The goal is not to generate more code. It is to remain in control after code volume explodes—to understand why the system is designed this way, how correctness is proven, where to start when results diverge, and how each lesson becomes a reusable, testable skill.

## 47. 公开调研参考：用于维护 related-work.md
说明：以下为 2026 年 7 月公开可检索样本，用于识别重叠和建立引用，不代表对 GitHub 或 LinkedIn 的穷尽性盘点。

**•** [GitHub Spec Kit：Spec-driven development](https://github.com/github/spec-kit) — 规格、计划、任务、实现和项目 Constitution 的代表性开源工作流。

**•** [GitHub Resources：Spec-driven development with AI](https://resources.github.com/increasing-collaborative-development-with-ai/) — GitHub 对规格驱动 AI 开发流程的官方介绍。

**•** [Addy Osmani：Agent Skills](https://github.com/addyosmani/agent-skills) — 把生产级工作流和质量门编码为 Agent Skill。

**•** [Paul Duvall：AI Development Patterns](https://github.com/PaulDuvall/ai-development-patterns) — 按生命周期整理 AI 辅助开发、测试、可观察性与运维模式。

**•** [OpenASE](https://github.com/PacificStudio/openase) — 强调 AI Coding Agent 需要由人保持控制的自动化工作流。

**•** [pytest 官方文档](https://docs.pytest.org/) — 从小型可读测试扩展到复杂功能测试的 Python 测试框架。

**•** [Playwright 官方文档](https://playwright.dev/) — 真实浏览器自动化、端到端测试与 Trace 证据。

**•** [Maestro 官方文档](https://docs.maestro.dev/) — 使用可读 YAML Flow 进行 iOS、Android 和 Web UI 自动化。

**•** [OpenTelemetry：Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) — 从系统外部理解内部行为，并通过 Logs、Metrics、Traces 诊断未知问题。

**•** [GitHub Discussions 官方文档](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions) — 用开放式讨论管理方向、问答和社区意见。

**•** [GitHub：Licensing a repository](https://docs.github.com/articles/licensing-a-repository) — 公开仓库要成为真正可使用、修改和分发的开源项目，需要明确许可证。

**•** [OpenClaw 官方项目](https://github.com/openclaw/openclaw) — OpenClaw 的安装、Gateway、Channel 与 Skill 入口。

**•** [OpenClaw 官方安全文档](https://docs.openclaw.ai/gateway/security) — 强调 Skill 文件夹应视作受信任代码并限制修改权限。

**•** [LinkedIn：AI-assisted software engineering fundamentals](https://www.linkedin.com/posts/allenholub_one-of-the-main-points-of-resistance-to-ai-assisted-activity-7411120032409124864-PSBA) — 代表性观点：AI 速度提升需要同步加强规划、测试、CI/CD 与安全。

**•** [LinkedIn：Building with AI, and What It Taught Me](https://www.linkedin.com/pulse/building-ai-what-taught-me-simon-ince-muece) — 真实项目中自动 Review、iOS UI 测试和多层 QA 的相近实践。
