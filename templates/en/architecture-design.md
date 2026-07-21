# Architecture design

> System / change:  
> Architecture owner:  
> Status: Proposed / Approved / Implemented / Superseded  
> Related requirements:  
> Last updated:

## 1. Decision summary

State the architecture in plain language, the key trade-off, and why the design fits this specific context.

## 2. Context and constraints

- Product and business constraints:
- Workload and performance budgets:
- Security, privacy, compliance, and tenant constraints:
- Existing systems and migration constraints:
- Team, operations, cost, and time constraints:
- Decisions already fixed outside this document:

## 3. System context

Describe users, operators, devices, third-party systems, data sources, and trust boundaries. Add a diagram whose nodes and arrows are explained in text.

## 4. Component model

| Component | Responsibility | Inputs / outputs | State owned | Scaling unit | Failure impact |
|---|---|---|---|---|---|
| | | | | | |

Each responsibility should have one clear owner. Identify duplicated authority or ambiguous state ownership.

## 5. Critical flows

For every high-risk or high-volume flow, document:

1. entry condition;
2. authentication and authorization;
3. state transitions;
4. synchronous and asynchronous boundaries;
5. external calls;
6. timeout, retry, idempotency, and deduplication;
7. observability points;
8. failure response and recovery;
9. user-visible outcome.

## 6. Data architecture

- Sources of truth:
- Data ownership by component:
- Transaction boundaries:
- Consistency model:
- Caching and invalidation:
- Data lifecycle, retention, and deletion:
- Analytics/ML separation from operational data:
- Schema and migration strategy:

## 7. Interface contracts

Link API, event, database, device, file, and model contracts. Identify versioning and compatibility guarantees.

## 8. AI and algorithm boundaries

- Where AI is used and where deterministic logic is required:
- Model inputs, outputs, confidence, and fallback:
- Human approval or override:
- Prompt/model/skill versioning:
- Evaluation and monitoring:
- Data leakage and prompt-injection boundaries:

## 9. Reliability and failure modes

| Failure mode | Detection | Containment | Recovery | User impact | Owner |
|---|---|---|---|---|---|
| | | | | | |

Include dependency outage, partial success, duplicate events, stale cache, split state, network loss, device unavailability, model degradation, and operational mistakes where applicable.

## 10. Security and privacy architecture

- Assets and trust boundaries:
- Authentication, authorization, and least privilege:
- Tenant and environment isolation:
- Secret handling:
- Audit trail:
- Data minimization and redaction:
- Supply-chain and plugin/skill controls:

## 11. Performance model

- Critical path and latency budget allocation:
- Expected query and access patterns:
- Concurrency and backpressure:
- Hot partitions, fan-out, N+1, and large payload risks:
- Baseline and load-test plan:

## 12. Deployment and operations

- Runtime topology and environments:
- Configuration and secret promotion:
- Rollout, migration, and rollback:
- Observability and alert ownership:
- AI operational authority by environment:

## 13. Alternatives and rejected designs

| Alternative | Advantages | Disadvantages | Evidence / uncertainty | Why rejected |
|---|---|---|---|---|
| | | | | |

Avoid choosing technology because it is popular or because an AI generated a confident comparison. Tie the decision to workload, constraints, experience, and tests.

## 14. Validation plan

List architecture spikes, benchmarks, failure injection, security review, prototype tests, and unknowns that must be resolved before full implementation.

## 15. Approval and change control

- Approved by:
- Approval date:
- Related ADRs:
- Conditions of approval:
- Triggers for revisiting the architecture:
