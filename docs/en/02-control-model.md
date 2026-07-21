# The four-plane control model

Traditional development often treats code production as the center of the system. In AI-assisted development, the stable center is a feedback loop between control, execution, evidence, and learning.

## The four planes

| Plane | Human responsibility | Best use of AI | Typical artifacts |
|---|---|---|---|
| Control | Define value, requirements, boundaries, architecture, algorithms, risk, and acceptance | Organize input, expose ambiguity, generate options, compare trade-offs | PRD, NFR, ADR, API contracts, data definitions, implementation plans, skills |
| Execution | Approve scope, guard irreversible actions, resolve critical exceptions | Implement, refactor, write tests, run tools, update documentation | Code, configuration, migrations, tests, builds |
| Evidence | Define what correctness means and decide whether evidence is sufficient | Execute checks, collect artifacts, compare results, isolate suspicious paths | Test reports, logs, traces, metrics, benchmarks, recordings, review reports |
| Learning | Decide which lessons are durable and own organizational memory | Cluster failure patterns, draft retrospectives, generate skill/test updates | Regression tests, retrospectives, skills, templates, case studies |

The planes form a closed loop:

```text
CONTROL sets boundaries
    ↓
EXECUTION produces a change
    ↓
EVIDENCE challenges the change
    ↓
LEARNING updates future control
    └───────────────→ CONTROL
```

A missing plane has predictable consequences:

- Without control, the agent optimizes an incomplete interpretation.
- Without bounded execution, unrelated changes and hidden complexity accumulate.
- Without evidence, plausible output is mistaken for correct output.
- Without learning, the same failure returns in another task or project.

## The ten-stage lifecycle

| Stage | Name | Governing question |
|---|---|---|
| 0 | Problem and value | Why are we building this, for whom, and what will we not build? |
| 1 | Requirements | Which scenarios, rules, states, exceptions, and acceptance criteria define success? |
| 2 | Non-functional requirements and risk | What must be true about performance, security, privacy, reliability, cost, compatibility, and operations? |
| 3 | Design and architecture | How are UI, API, modules, data, algorithms, deployment, and evolution structured? |
| 4 | Decomposition and implementation plan | What is the smallest safe change, which files and interfaces move, and how will it be verified? |
| 5 | Implementation and local checks | Can the agent implement only the approved scope and pass static/unit checks immediately? |
| 6 | System and adversarial validation | Do independent, end-to-end, contract, property, regression, and failure tests support the claim? |
| 7 | Observability and diagnosis | Can we reconstruct the actual execution and find the first divergence? |
| 8 | Performance, release, and operations | Are budgets met, migrations safe, rollout controlled, and rollback rehearsed? |
| 9 | Retrospective and skill capture | What must change in documents, tests, templates, or skills so the class of failure does not recur? |

## Control does not mean micromanagement

The objective is not to prescribe every line or prevent useful agent judgment. Good control defines invariants, boundaries, evidence, and stop conditions, then gives the agent freedom inside those limits. Too little control produces drift. Too much low-level instruction produces brittle work and prevents the agent from using its strengths.

The practical balance is:

- humans specify the **what**, **why**, constraints, and irreversible decisions;
- agents propose and execute the **how** within an approved plan;
- evidence determines whether a lifecycle transition is allowed;
- failure updates the next cycle.
