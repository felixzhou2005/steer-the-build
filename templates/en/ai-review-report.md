# AI-native review report

> Change / commit / PR:  
> Review agent/model/version:  
> Review instructions/skills:  
> Evidence snapshot:  
> Human risk owner:

AI review supplements automated tools and focused human judgment. It is not proof by itself. Findings must point to code, contracts, tests, or runtime evidence.

## 1. Review scope

- Requirements and acceptance criteria reviewed:
- Architecture/ADRs reviewed:
- Files and commits reviewed:
- Tests, logs, traces, metrics, and benchmarks reviewed:
- Areas explicitly excluded:

## 2. Architecture consistency

| Finding | Severity | Evidence | Impact | Required action |
|---|---|---|---|---|
| | | file/line/diagram | | |

Check boundaries, ownership, dependency direction, public contracts, state duplication, data flow, migration compatibility, and unnecessary abstraction.

## 3. Functional coverage

Map implementation and tests to requirements, business invariants, UI states, error paths, and recovery.

| Requirement | Implementation evidence | Test evidence | Gap |
|---|---|---|---|
| | | | |

## 4. Implementation quality

Review correctness, simplicity, readability, error handling, concurrency, resource handling, dependency use, configuration, and maintainability. Do not equate style preference with defect severity.

## 5. Security and privacy

Review authentication, authorization, tenant isolation, injection, secrets, sensitive logging, retention, unsafe tool use, supply chain, and production authority.

## 6. Performance and capacity

Review query/access patterns, allocations, blocking operations, fan-out, N+1, caching, payloads, retries, timeouts, and whether measured evidence supports the design.

## 7. Test quality and independence

- Do tests derive expected behavior from requirements or from the implementation?
- Are negative, boundary, recovery, and concurrency paths represented?
- Could the implementation and tests share the same wrong assumption?
- Are UI/mobile flows tested in a representative environment?
- What still requires human or production-like validation?

## 8. Observability and diagnosis

Determine whether a future operator or AI agent can locate the first divergence using logs, traces, metrics, versions, and correlation IDs without exposing sensitive data.

## 9. Findings summary

| ID | Severity | Category | Description | Blocking? | Owner |
|---|---|---|---|---|---|
| R-001 | Critical/High/Medium/Low/Note | | | Yes/No | |

Severity should reflect consequence and likelihood, not how confidently the reviewer writes.

## 10. Residual risk and human review

Identify decisions that cannot be delegated to the review agent, including business invariants, visual quality, algorithm direction, destructive operations, data migration, and accepted risk.

## 11. Verdict

- `PASS` — required evidence is present and no blocking finding remains.
- `PASS WITH EXCEPTIONS` — exceptions are explicit, owned, and approved.
- `FAIL` — blocking findings or missing evidence remain.
- `INCONCLUSIVE` — the reviewer lacks required context or evidence.

Verdict:  
Blocking items:  
Human approval:  
Date:
