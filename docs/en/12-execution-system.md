# An executable AI-native engineering system

Principles become useful only when they create mandatory artifacts and gates.

## Minimum project artifacts

A non-trivial project should maintain:

1. problem/value brief;
2. product requirements and non-goals;
3. non-functional requirements and risk register;
4. architecture and key ADRs;
5. UI, API, data, and algorithm specifications as applicable;
6. project AI constitution and skill set;
7. implementation plans for each change;
8. automated test and evidence strategy;
9. observability specification;
10. release, rollback, and operations runbook;
11. incident and retrospective records;
12. a trace from requirements to tests and current behavior.

The templates in this repository are intended to make these artifacts cheap to start and consistent to review.

## The eight-step task loop

### 1. Frame

State the requirement, non-goals, source documents, risk class, and acceptance criteria.

### 2. Inspect

Ask the agent to inspect the current repository and report relevant architecture, behavior, tests, and uncertainty. No edits yet.

### 3. Plan

Produce a detailed implementation and verification plan with affected files, interfaces, migration, observability, and rollback.

### 4. Approve

A human corrects the plan, resolves trade-offs, and explicitly authorizes scope.

### 5. Implement

The agent changes only the approved area, keeps the diff bounded, and updates tests and documentation in the same task.

### 6. Verify

Run static, unit, integration, end-to-end, performance, and risk-appropriate checks. Capture failure and success artifacts.

### 7. Review

Use an independent reviewer context for architecture, requirements, implementation, security, performance, and evidence. A human resolves high-risk findings.

### 8. Learn

Record the result, update the regression suite and documents, and convert repeated lessons into a skill or template.

## Autonomy levels

| Level | Agent authority | Suitable work |
|---|---|---|
| A0 — Advise | Research and propose only | Architecture, algorithms, high-risk design |
| A1 — Draft | Create plans or files, no execution | Specifications, migration drafts, UI proposals |
| A2 — Execute locally | Edit and run in a disposable/local environment | Most bounded implementation tasks |
| A3 — Execute with gates | Operate shared test/staging through approved workflows | Integration, deployment rehearsal, non-destructive cloud work |
| A4 — Production assist | Generate plans/scripts and observe production; humans approve execution | High-risk diagnosis and controlled change |
| A5 — Bounded production automation | Deterministic, pre-approved operations within strict policy | Mature low-risk runbooks only |

Autonomy must be revocable. An agent should stop when scope, evidence, environment, or permission is uncertain.

## Definition of Done

An AI-assisted task is done only when:

- the approved requirement and non-goals are satisfied;
- the implementation matches the reviewed plan or deviations are documented;
- architecture and public contracts remain consistent;
- tests are meaningful, executed, and linked to the exact revision;
- relevant end-to-end or real-environment behavior is captured;
- performance and security requirements are addressed;
- logs, traces, metrics, and diagnostic fields are sufficient;
- migrations, release, and rollback are handled;
- documentation is current;
- known limitations and residual risk are explicit;
- required human approval is recorded;
- any reusable lesson has been considered for a test, template, or skill.

## Measuring the “10×” claim responsibly

A personal tenfold improvement may be real, but the metric must include the whole system. Track:

- lead time from accepted requirement to usable version;
- active human hours, including planning, review, and diagnosis;
- first-pass acceptance rate;
- number and severity of rework cycles;
- escaped defects, incidents, and rollback;
- time to isolate and recover from failure;
- maintenance cost for later changes;
- model, infrastructure, test-device, and observability spend;
- business adoption or operational savings;
- reuse of templates and skills.

A speed improvement that creates later instability is not a tenfold engineering improvement. It is a transfer of cost.
