# Project AI constitution

> Status: Draft / Approved / Superseded  
> Owner: `<name>`  
> Version: `<version>`  
> Last reviewed: `<YYYY-MM-DD>`

This file defines the persistent rules for AI agents working in this repository. Keep it short enough to load reliably, strict enough to prevent recurring failure, and linked to detailed documents rather than duplicating them.

## 1. Project intent

- Product or system purpose:
- Primary users:
- Business or technical outcomes:
- Explicit non-goals:
- Highest-consequence failures:

## 2. Source of truth and precedence

When instructions conflict, use this order:

1. safety, legal, privacy, and production controls;
2. approved product requirements and acceptance criteria;
3. approved architecture decisions and interface contracts;
4. project-level skills and coding standards;
5. task-specific implementation plan;
6. local code conventions inferred from the repository.

Do not silently resolve a material conflict. Stop and report the conflicting sources, impact, and recommended decision.

## 3. Required workflow

For every non-trivial change:

1. Read the relevant requirements, design, interfaces, tests, and recent decisions.
2. Restate scope, non-goals, assumptions, and acceptance criteria.
3. Produce a bounded implementation plan before editing.
4. Identify affected modules, contracts, data, migrations, tests, observability, and rollback.
5. Implement in small reviewable steps.
6. Run the required static checks and automated tests.
7. Review behavior, architecture, security, performance, and failure paths.
8. Provide evidence, changed files, known limitations, and documentation updates.
9. Do not declare completion while required evidence is missing or failing.

## 4. Human-owned decisions

The agent may analyze and recommend, but must not finalize these decisions without explicit approval:

- product scope or acceptance criteria;
- architecture or technology choices with material lock-in;
- complex algorithm/model direction and evaluation standard;
- visual theme, brand expression, or intentional deviation from Figma;
- data retention, privacy, authorization, or tenant boundaries;
- production deployment, destructive operations, irreversible migration, or external communication;
- any trade-off that changes risk, cost, latency, accuracy, or user impact.

## 5. Simplicity and implementation boundaries

- Implement the approved requirement, not imagined future requirements.
- Prefer the simplest design that satisfies current constraints and measured workload.
- Do not add abstractions, frameworks, dependencies, fallback paths, or generic configuration without a stated need.
- Preserve established module boundaries and public contracts unless a reviewed plan changes them.
- Avoid broad cleanup inside a feature change unless it is required and separately identified.
- For SQL, optimize for correct semantics, clear access patterns, and measured performance; avoid unnecessary nesting and defensive complexity.

## 6. Quality and evidence

Required checks for this project:

- Static analysis / formatter:
- Unit and component tests:
- API/integration tests:
- Browser/UI tests:
- Mobile tests:
- Performance checks:
- Security checks:
- Documentation checks:

Test expectations must come from approved requirements, business invariants, real examples, golden data, differential behavior, or another independent oracle—not only from the implementation being tested.

## 7. Observability

Every material flow must expose enough evidence for human and AI diagnosis. As applicable, include:

- correlation or trace ID;
- anonymized user, tenant, device, job, and model identifiers;
- state transitions and decision outcomes;
- dependency timing, retries, fallbacks, and error classification;
- model, prompt, skill, configuration, and deployment versions;
- privacy-safe context needed to reproduce the failure.

Never log secrets, raw credentials, unnecessary personal data, or unredacted sensitive content.

## 8. Failure and retry policy

Do not repeatedly modify code because a top-level result is wrong. After `<N>` failed attempts or any sign of circular reasoning:

1. stop changing the implementation;
2. preserve the failing input and evidence;
3. decompose the result into smaller observable stages;
4. locate the first divergence from expected behavior;
5. test competing root-cause hypotheses;
6. update the plan before resuming.

## 9. Operations

- Development environment authority:
- Test/staging authority:
- Production authority:
- Commands requiring human approval:
- Backup and rollback requirements:
- Secret-management rules:
- Audit-log location:

AI may prepare and validate production scripts in a controlled environment. It must not cross the production approval boundary defined above.

## 10. Definition of done

A task is done only when:

- acceptance criteria are mapped to passing evidence;
- required review dimensions have passed or have approved exceptions;
- migrations and rollback have been tested where relevant;
- logs, metrics, and alerts support the new behavior;
- documentation and skills reflect the implemented reality;
- known limitations and residual risks are explicit;
- the human owner accepts the result.
