# Layered skills and engineering memory

A skill is more than a saved prompt. It is a versioned unit of engineering policy that tells an agent when a rule applies, what behavior is required, what is forbidden, how success is verified, and what exceptions exist.

## Skill layers

| Layer | Scope | Examples |
|---|---|---|
| Base | Stable principles used across projects | plan before code, simple by default, evidence before done, documentation sync, no blind retry |
| Domain / stack | A technology or engineering discipline | efficient SQL, pytest quality, Playwright evidence, Maestro mobile flows, Figma fidelity, ML evaluation |
| Project | Architecture and business rules unique to one system | module boundaries, tenant model, state machine, naming, deployment, device constraints |
| Task | Temporary instructions for one bounded change | allowed files, migration sequence, acceptance criteria, rollback, experiment input |

Base skills should be small and durable. Project skills should make the repository's unique decisions explicit. Task skills should expire or be absorbed into a higher layer after the work.

## A complete skill specification

A useful skill includes:

- purpose and problem class;
- trigger conditions;
- non-trigger conditions;
- required inputs and source-of-truth documents;
- ordered workflow;
- mandatory rules and prohibited behaviors;
- output format and evidence;
- positive and negative examples;
- known limitations and compatibility;
- owner, version, change history, and deprecation status;
- tests or historical failures used to validate it.

## Examples from practice

**Figma fidelity**: implement approved Figma screens with exact structure, spacing, typography, color, states, and responsive behavior. Do not invent missing design choices silently. Surface ambiguities, capture screenshots, and compare the result before declaring completion.

**Simple, efficient SQL**: implement the required behavior with the simplest readable query; avoid speculative fallbacks and unnecessary joins; use known constraints; explain indexes and cardinality; provide a query plan for high-impact paths.

**Evidence before done**: completion requires the exact source revision, linked requirement, tests, relevant runtime artifacts, known gaps, and reviewer decision. A textual “works now” claim is insufficient.

**Observability first**: every new critical path must expose stable event names, correlation IDs, state transitions, external-call timing, reason codes, and privacy handling before the feature is considered operable.

## From defect to skill

A problem should not end with a local patch. Use this loop:

1. Identify the root cause, not only the symptom.
2. Ask why existing requirements, tests, review, or skills failed to prevent it.
3. Choose the right durable control: document clarification, regression test, static rule, template field, or skill update.
4. Test the new control against the historical failure.
5. Check that it does not over-constrain legitimate cases.
6. Version and record the change.
7. Monitor recurrence and retire ineffective rules.

This creates compound improvement: every project teaches the agents and the human workflow how to avoid a known class of error.

## Skill governance

A large skill collection can become contradictory, stale, or too expensive to load. Manage it like code:

- assign an owner and version;
- define precedence when skills conflict;
- keep stable base skills separate from project context;
- test triggers and non-triggers;
- record model/tool compatibility;
- review usage and failure data;
- deprecate duplicates;
- avoid broad rules that mask missing requirements;
- do not allow a skill to change acceptance criteria or production authority implicitly.

The value of a skill is not how polished its prose sounds. It is whether it consistently prevents a real error or produces a useful, verifiable behavior.
