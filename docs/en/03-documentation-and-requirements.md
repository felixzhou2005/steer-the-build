# Documentation, requirements, and lifecycle

## Start with the problem, not the implementation

A project should begin by answering:

- Who has the problem?
- What is the current workflow and cost?
- Which outcome would create measurable value?
- Which assumptions are unverified?
- What is explicitly out of scope?
- What would cause the project to stop?

AI makes it dangerously cheap to implement the wrong idea. Fast implementation can delay discovery that the product direction is wrong because visible progress creates false confidence. Early research should therefore include customer evidence, process observation, baseline measurements, competing approaches, and a decision about whether software is the right intervention.

## Requirements must be executable by another mind

A useful requirement is not “build a dashboard” or “make the UI professional.” It describes behavior well enough that a human reviewer and an AI agent can independently determine whether the result is correct.

A minimum executable requirement set includes:

- user and system actors;
- primary and alternate journeys;
- business rules and invariants;
- state transitions;
- inputs, outputs, and data semantics;
- permissions and ownership;
- errors, timeouts, retries, and recovery;
- compatibility and migration expectations;
- acceptance criteria and non-goals.

Hidden defaults are common failure sources. Examples include timezone, ordering, rounding, duplicate handling, empty states, cancellation behavior, offline state, idempotency, and what happens when an external system partially succeeds.

## Documentation is an engineering control plane

An AI system consumes text, code, schemas, tests, and tool output as context. If the reasoning that produced a decision exists only in a person's head or a long chat, it is not a durable project artifact.

The documentation chain should connect:

```text
Problem → Requirements → NFRs → Architecture → Detailed design
       → Implementation plan → Tests → Release → Operations → Retrospective
```

Each document answers a different question. Collapsing them into one giant prompt causes omission and makes change control difficult.

| Artifact | Purpose |
|---|---|
| Product brief / PRD | Value, users, scope, journeys, non-goals, acceptance |
| NFR specification | Performance, security, reliability, privacy, cost, compatibility, operability |
| Architecture document | Components, boundaries, dependencies, deployment, failure domains |
| ADR | A specific decision, alternatives, evidence, trade-off, and consequences |
| UI/Figma specification | Visual source of truth, states, interactions, responsive and accessibility requirements |
| API contract | Endpoints, schemas, errors, idempotency, versioning, authorization |
| Data dictionary | Table and field semantics, ownership, lineage, retention, constraints |
| Algorithm design | Objective, assumptions, baseline, data, metrics, experiments, failure modes |
| Implementation plan | Scope, files, sequence, interfaces, tests, risks, rollback |
| Test plan | Independent oracle, layers, cases, environments, artifacts, exit criteria |
| Observability specification | Events, identifiers, traces, metrics, decision reasons, privacy |
| Runbook | Deployment, rollback, incident actions, ownership, escalation |

## Textualizing the thinking process

People often resist this documentation because it feels slower than asking an agent to start. In practice, the human is already thinking through these issues. Writing them down prevents the common pattern of solving one concern, forgetting an earlier constraint, and allowing the agent to fill gaps with generic assumptions.

A productive interaction is not “AI, derive the entire system.” It is iterative externalization:

1. The human explains the current understanding.
2. The agent organizes it and identifies ambiguity.
3. The human makes choices and adds context.
4. The document is revised until it can guide implementation.
5. The implementation and evidence feed back into the document.

## Keep documents alive

Documents must be versioned beside the system and updated in the same change as behavior. When code and documentation disagree, the team must determine which represents current truth, correct the other, and record why the drift occurred. A stale specification can be more dangerous than no specification because it confidently directs the agent toward obsolete behavior.

Recommended controls include:

- link requirements to tests and implementation tasks;
- include “last reviewed” and owner fields for high-risk documents;
- require documentation impact in implementation plans and pull requests;
- store field semantics and state rules close to schemas;
- use ADRs for decisions that should not be silently reversed;
- archive superseded versions rather than stacking contradictory patches.
