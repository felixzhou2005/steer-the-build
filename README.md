# Steer the Build

> **AI builds. Humans steer. Evidence decides.**
>
> A bilingual, open field guide to human-controlled, evidence-driven AI software engineering at scale.

[Complete Chinese methodology](docs/zh-CN/full-book.md) · [English methodology](docs/en/index.md) · [简体中文](README.zh-CN.md) · [Templates](templates/README.md) · [Quick start](QUICKSTART.md) · [Repository structure](PROJECT_STRUCTURE.md)

## Why this project exists

AI coding agents can now generate, refactor, test, review, and operate far more code than a human can reasonably read line by line. That changes the engineering bottleneck. The hard problem is no longer typing code. It is keeping intent, architecture, quality, runtime behavior, and responsibility under control while implementation volume accelerates.

This project documents a method developed across business systems, mobile apps, machine learning, voice systems, IoT and hardware-adjacent projects, cloud deployment, and reusable agent skills. Based on the maintainer's current cross-project estimate, AI generated more than 300,000 lines of application code without the maintainer hand-writing that code. The counting method has not yet been independently audited, so this is a personal practice estimate rather than a benchmark or universal performance claim. Its importance is structural: once implementation is heavily delegated, the engineering control system becomes the primary work product.

## The central thesis

> Coding can be delegated. Engineering accountability cannot.

Humans own:

- the problem, value, scope, and non-goals;
- architecture, algorithmic direction, product taste, and trade-offs;
- risk, evidence standards, release authority, and consequences.

AI is used to:

- research and compare options;
- produce implementation plans and code;
- run tests and tools;
- review architecture, behavior, and implementation;
- inspect logs, traces, metrics, and failures;
- execute repetitive development and test operations.

## The method in one loop

```text
INTENT → SPECIFY → DESIGN → PLAN → BUILD → REVIEW → TEST → OBSERVE → DIAGNOSE → LEARN
   ↑                                                                          │
   └────────────────────── update documents, tests, and skills ──────────────┘
```

The method is organized around four planes:

| Plane | Purpose | Main artifacts |
|---|---|---|
| Control | Define intent, boundaries, architecture, risk, and acceptance | Requirements, NFRs, ADRs, contracts, plans, skills |
| Execution | Let agents implement within approved scope | Code, configuration, migrations, tests, build artifacts |
| Evidence | Prove behavior instead of trusting fluent output | Tests, logs, traces, metrics, benchmarks, review reports |
| Learning | Convert every success and failure into reusable control | Retrospectives, regression tests, templates, versioned skills |

## Start here

1. Start with the [English methodology](docs/en/index.md), or read the [complete Chinese methodology](docs/zh-CN/full-book.md).
2. Use the [lifecycle and documentation model](docs/en/03-documentation-and-requirements.md) before asking an agent to implement.
3. Apply [AI-native review](docs/en/05-ai-native-review.md), [automated testing](docs/en/06-testing.md), and [AI-readable observability](docs/en/07-observability-and-debugging.md).
4. Copy the [project AI constitution](templates/en/project-ai-constitution.md) and the other templates into a real repository.
5. Use the [skill specification template](templates/en/skill-spec.md) to turn repeated lessons into governed, testable instructions.
6. Add evidence-backed experience through the [contribution process](CONTRIBUTING.md).

## What makes this different

This is not a prompt collection, a coding-agent leaderboard, or a claim that autonomous agents can own production systems. Its focus is the operating method required when:

- code volume is too large for exhaustive human line-by-line review;
- architecture, product taste, algorithms, or physical systems require expert judgment;
- correctness must be demonstrated through independent tests and runtime evidence;
- logs and traces are designed for both human and AI diagnosis;
- defects are converted into persistent skills and quality gates;
- AI is allowed to perform development operations, but production remains risk-gated.

## Repository map

| Path | Purpose |
|---|---|
| `docs/en/`, `docs/zh-CN/` | Bilingual method and long-form guide |
| `templates/` | Requirements, architecture, planning, review, testing, observability, release, incident, and case templates |
| `research/` | Related work, differentiation, terminology, and source-review policy |
| `meta/` | Editorial, translation, release, and post-creation checklists |

## Project status

The public **v0.1 foundation** is methodology-first: the bilingual method, templates, related-work notes, governance, quality checks, and documentation site are included. Evidence-backed cases, validated real-world skills, and publication drafts remain local until they are reviewed and ready for a later release.

See the [roadmap](ROADMAP.md) and [content status](meta/content-status.md).

## Contributing

Contributions are welcome when they add evidence, not just opinions. The preferred forms are:

- a real case or counterexample;
- a reproducible failure and root-cause analysis;
- a skill validated against historical mistakes;
- a template used in a real project;
- a precise related-work comparison;
- a reviewed translation tied to a source commit.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License

Documentation and explanatory prose are licensed under **CC BY 4.0**. Reusable templates and configuration examples are licensed under **MIT**. See [LICENSES.md](LICENSES.md).
