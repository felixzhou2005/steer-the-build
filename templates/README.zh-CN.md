# 工程模板

[English](README.md)

这些模板把方法论变成可以审查的工程产物。它们不绑定具体工具。应根据项目风险和复杂度选用需要的模板；不适用的条目应明确删除或写明不适用，而不是留下含糊空白。

## 不同风险项目的最小组合

| 项目类型 | 建议最小文档集 |
|---|---|
| 小型、可逆的内部工具 | 产品需求、任务卡、测试策略、实现方案 |
| 面向客户的业务系统 | 上述内容 + NFR、架构、API/数据设计、可观察性、发布与回滚 |
| Mobile App | 上述内容 + UI 设计规格、设备测试矩阵、发布质量门 |
| ML 或复杂算法 | 上述内容 + 算法/ML 设计、基线、评估数据集、误差分析 |
| 语音、IoT 或硬件相关系统 | 上述内容 + 安全状态、指令授权、失败模式、设备与延迟证据 |
| 多租户或生产级 Agent 服务 | 上述内容 + 安全隐私、租户隔离、Skill/Plugin 治理和事故预案 |

## 模板目录

| 模板 | 主要保护的决策 |
|---|---|
| [项目 AI 宪法](zh-CN/project-ai-constitution.md) | AI 可以做什么、必须证明什么、不得自行推断什么 |
| [产品需求](zh-CN/product-requirements.md) | 项目真正负责的问题和结果 |
| [非功能需求](zh-CN/non-functional-requirements.md) | 性能、可靠性、安全、隐私、无障碍和成本边界 |
| [架构设计](zh-CN/architecture-design.md) | 系统边界、数据流、取舍和失败模式 |
| [架构决策记录](zh-CN/architecture-decision-record.md) | 一个重要选择及其替代方案 |
| [UI 设计规格](zh-CN/ui-design-spec.md) | Figma 高保真、状态、交互、无障碍和视觉例外 |
| [API 设计](zh-CN/api-design.md) | 契约、语义、错误、幂等、兼容性和授权 |
| [数据库设计](zh-CN/database-design.md) | 数据含义、约束、访问模式、迁移和性能 |
| [算法与 ML 设计](zh-CN/algorithm-and-ml-design.md) | 问题建模、基线、指标、数据、模型选择和误差分析 |
| [实现方案](zh-CN/implementation-plan.md) | 一个有边界的修改怎样实现和验证 |
| [任务卡](zh-CN/task-card.md) | 一个适合 AI 独立执行的工作单元 |
| [AI Review 报告](zh-CN/ai-review-report.md) | 架构、功能、实现、安全和证据审查 |
| [测试策略](zh-CN/test-strategy.md) | 多层独立证据与覆盖范围 |
| [可观察性规格](zh-CN/observability-spec.md) | 理解和诊断运行过程所需的信号 |
| [性能计划](zh-CN/performance-plan.md) | 工作负载、预算、基线、Profiling 和回归质量门 |
| [安全与隐私审查](zh-CN/security-privacy-review.md) | 资产、信任边界、滥用方式、隐私和生产权限 |
| [发布与回滚](zh-CN/release-and-rollback.md) | 修改如何进入生产以及如何安全撤销 |
| [事故分析](zh-CN/incident-analysis.md) | 时间线、影响、第一个偏差点、根因和系统性预防 |
| [Skill 规格](zh-CN/skill-spec.md) | 重复经验怎样成为版本化的 AI 控制能力 |
| [案例研究](zh-CN/case-study.md) | 项目经验怎样成为公开、可验证的知识 |

## 使用原则

不要把一个模糊想法交给 AI，让它一次性填完全部模板，然后把流畅的文字当成已批准设计。人的 Owner 应先提供意图、约束、取舍和未决问题；AI 可以负责结构化、质疑和补全；实现前再由人批准文档。

模板和示例 Skill 采用 MIT 许可证，详见 [LICENSES.md](../LICENSES.md)。
