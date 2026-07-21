# Templates and prompts

The repository separates durable method from reusable working artifacts.

## Templates

Use the bilingual files under [`templates/`](../../templates/README.md) as starting points for:

- product requirements and non-functional requirements;
- architecture decisions, API, database, and algorithm design;
- implementation plans and project AI constitutions;
- AI-native review and test plans;
- observability and performance specifications;
- release, rollback, and incident analysis;
- skills and public case studies.

Templates are intentionally structured as questions and required evidence. Delete sections only after deciding that they do not apply; do not let an agent silently omit them.

## Prompt pattern: inspect before editing

```text
Read the linked requirement, architecture, ADRs, and relevant project skills.
Inspect the repository without making changes.
Report:
1. current behavior and the path that implements it;
2. affected modules, interfaces, data, and tests;
3. ambiguities or conflicts in the source documents;
4. risks, especially security, migration, concurrency, and performance;
5. the smallest implementation slices you recommend.
Do not write code yet.
```

## Prompt pattern: implementation plan gate

```text
Create a detailed implementation plan for the approved requirement.
Include scope and non-goals, exact files and interfaces, data/state changes,
migration and compatibility, failure handling, observability, tests and evidence,
documentation updates, rollback, and unresolved decisions.
Prefer the simplest design that satisfies current requirements.
Do not introduce abstractions for unspecified future use.
Wait for plan approval before implementation.
```

## Prompt pattern: bounded implementation

```text
Implement only the approved plan.
Do not modify unrelated files or acceptance criteria.
After each slice, run the focused checks and report the exact evidence.
If repository reality conflicts with the plan, stop and explain the conflict
instead of improvising a new architecture.
Update tests and documentation in the same change.
```

## Prompt pattern: independent AI review

```text
Act as an independent reviewer. Treat the implementation summary as a claim,
not as truth. Reconstruct the change from the diff, source requirements, and
runtime evidence. Review architecture, requirement coverage, implementation,
security, performance, failure paths, tests, and observability separately.
For every finding, state severity, affected invariant, exact path or condition,
evidence, and the smallest safe remediation. List unverified areas explicitly.
```

## Prompt pattern: reverse diagnosis

```text
Do not propose a fix yet. Freeze the input, environment, source revision,
configuration, model/data/skill versions, expected result, and actual result.
Break the workflow into observable stages and identify the earliest divergence.
Generate at most three competing hypotheses and the cheapest experiment that
would distinguish them. Request additional instrumentation where evidence is
missing. Stop random retrying.
```

## Prompt pattern: skill extraction

```text
Analyze this incident and determine whether the lesson should become a
requirement clarification, regression test, static rule, template field, or
versioned skill. If a skill is justified, define its trigger and non-trigger,
mandatory rules, forbidden behavior, examples, evidence, limitations, owner,
and a test using the historical failure. Avoid a rule that overfits one case.
```

## Use prompts as entry points, not truth

A good prompt cannot compensate for missing product context, a wrong algorithm, weak data, or an invalid test oracle. Store the durable result—the requirement, plan, test, ADR, or skill—in the repository. Do not rely on a long chat as project memory.
