# Engineering templates

[简体中文](README.zh-CN.md)

These templates turn the method into inspectable artifacts. They are intentionally tool-neutral. Copy only the templates required by the risk and complexity of a project, then delete instructions that do not apply rather than leaving ambiguous blanks.

## Minimum set by project risk

| Project class | Recommended minimum |
|---|---|
| Small, reversible internal tool | Product requirements, task card, test strategy, implementation plan |
| Customer-facing business system | Above + NFRs, architecture, API/data design, observability, release/rollback |
| Mobile application | Above + UI design specification, device test matrix, release gates |
| ML or complex algorithm | Above + algorithm/ML design, baseline, evaluation dataset, error analysis |
| Voice, IoT, or hardware-adjacent | Above + safety states, command authorization, failure modes, device/latency evidence |
| Multi-tenant or production agent service | Above + security/privacy review, tenant isolation, skill/plugin governance, incident plan |

## Templates

| Template | Main decision it protects |
|---|---|
| [Project AI constitution](en/project-ai-constitution.md) | What the agent may do, must prove, and must not infer |
| [Product requirements](en/product-requirements.md) | What problem and outcome the project owns |
| [Non-functional requirements](en/non-functional-requirements.md) | Performance, reliability, security, privacy, accessibility, and cost boundaries |
| [Architecture design](en/architecture-design.md) | System boundaries, data flow, trade-offs, and failure modes |
| [Architecture decision record](en/architecture-decision-record.md) | One consequential choice and its alternatives |
| [UI design specification](en/ui-design-spec.md) | Figma fidelity, states, interaction, accessibility, and visual exceptions |
| [API design](en/api-design.md) | Contracts, semantics, errors, idempotency, compatibility, and authorization |
| [Database design](en/database-design.md) | Data meaning, constraints, access patterns, migrations, and performance |
| [Algorithm and ML design](en/algorithm-and-ml-design.md) | Problem framing, baseline, metrics, data, model choice, and failure analysis |
| [Implementation plan](en/implementation-plan.md) | How a bounded change will be implemented and verified |
| [Task card](en/task-card.md) | A single agent-sized unit of work |
| [AI review report](en/ai-review-report.md) | Architecture, behavior, implementation, security, and evidence review |
| [Test strategy](en/test-strategy.md) | Independent evidence and coverage across layers |
| [Observability specification](en/observability-spec.md) | Signals required to understand and diagnose runtime behavior |
| [Performance plan](en/performance-plan.md) | Workload, budget, baseline, profiling, and regression gates |
| [Security and privacy review](en/security-privacy-review.md) | Assets, trust boundaries, abuse cases, privacy, and production authority |
| [Release and rollback](en/release-and-rollback.md) | How change enters production and how it is safely reversed |
| [Incident analysis](en/incident-analysis.md) | Timeline, impact, first divergence, root causes, and systemic prevention |
| [Skill specification](en/skill-spec.md) | How a repeated lesson becomes a versioned agent control |
| [Case study](en/case-study.md) | How project experience becomes public, evidence-backed knowledge |

## Usage rule

Do not ask an agent to fill every template from a vague idea and then treat the result as approved design. The human owner should provide intent, constraints, trade-offs, and missing decisions; the agent may structure, challenge, and complete the document; the owner then approves the artifact before implementation.

Templates and example skills are licensed under MIT. See [LICENSES.md](../LICENSES.md).
