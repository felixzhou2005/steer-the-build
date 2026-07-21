# Related work

> Status: initial landscape scan for v0.1. This is a maintained comparison, not an exhaustive literature review.

Steer the Build overlaps with several active movements: specification-driven development, agent skills, AI development patterns, production-grade agent harnesses, automated testing, observability, secure development, and delivery performance. The table below explains the overlap and the boundary.

## Nearby projects and practices

| Source | Primary focus | Overlap with Steer the Build | Distinction or lesson adopted |
|---|---|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) | A toolkit for specification-driven development with AI coding agents | Separating specification, planning, tasks, and implementation | Steer the Build extends beyond specification into AI-native review, runtime evidence, reverse diagnosis, layered skills, release governance, and cross-domain cases |
| [Agent Skills by Addy Osmani](https://github.com/addyosmani/agent-skills) | Reusable skills for design, code quality, testing, performance, security, and workflows | Skills as persistent engineering instructions | This repository treats skills as a governed learning system: defect → rule → regression → skill version → historical validation |
| [AI Development Patterns](https://github.com/PaulDuvall/ai-development-patterns) | Patterns and anti-patterns for AI-assisted software delivery | Repeatable engineering patterns and quality practices | Steer the Build is organized around a four-plane control system and evidence-based authority, with bilingual templates and concrete case scaffolds |
| [Reins](https://github.com/WellDunDun/reins) | A harness for steering AI coding agents toward maintainable software | Explicit constraints and control around agents | This project is primarily a field guide and operating model rather than a single execution harness; it is tool- and model-agnostic |
| [Thoughtworks: Can vibe coding produce production-grade software?](https://thoughtworks.medium.com/can-vibe-coding-produce-production-grade-software-75130f25b63d) | Experiments comparing freeform prompting with deliberate engineering constraints | Human steering, modularity, testability, and maintainability | Steer the Build adds a full lifecycle, an AI-native review model for large code volumes, AI-readable observability, and skill feedback loops |

## Evidence and verification foundations

| Source | Role in this project |
|---|---|
| [pytest](https://docs.pytest.org/) | Representative Python unit, integration, property, and regression testing foundation |
| [Playwright](https://playwright.dev/docs/intro) | Browser-level critical-flow and end-to-end evidence |
| [Maestro](https://docs.maestro.dev/) | Mobile UI workflow automation and agent-driven flow execution |
| [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) | Shared vocabulary for logs, metrics, traces, context propagation, and system behavior |
| [DORA metrics](https://dora.dev/guides/dora-metrics/) | Delivery performance indicators that prevent “lines generated” from becoming the only productivity measure |
| [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) | Baseline for secure development responsibilities and practices |

## Agent operations and security

| Source | Relevance |
|---|---|
| [OpenClaw security guidance](https://docs.openclaw.ai/gateway/security) | Useful constraints for gateways, trusted operators, credentials, isolation, and deployment boundaries |
| [OpenClaw CLI security](https://docs.openclaw.ai/cli/security) | Reinforces treating skills and plugins as executable code and applying explicit permissions |
| [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills) | A practical reference for how reusable skills are packaged and invoked |

## What we intentionally do not claim

- That documentation alone guarantees a correct system.
- That AI review removes the need for human accountability.
- That human review should be eliminated from high-risk decisions.
- That one model or tool is universally superior.
- That all software can be built without software engineering experience.
- That every project should maximize autonomy.

## How to contribute related work

A useful addition should answer four questions:

1. What problem does the source solve?
2. Which Steer the Build principle overlaps?
3. What is materially different?
4. What should this project learn or change because of it?

Use the `related-work` label or open a pull request that updates this page and, where necessary, the corresponding Chinese page.
