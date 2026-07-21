# Implementation plan

> Change:  
> Plan owner:  
> Reviewer:  
> Status: Proposed / Approved / In progress / Complete  
> Related requirements / ADRs:

## 1. Goal and acceptance criteria

Restate the bounded outcome. Link every acceptance criterion to an evidence source.

## 2. Scope and non-goals

### In scope

- 

### Not in scope

- 

### Assumptions requiring validation

- 

## 3. Current-state analysis

- Relevant modules and entry points:
- Existing behavior and tests:
- Contracts, data, or state affected:
- Similar implementation to reuse:
- Known defects or technical debt that may interfere:

## 4. Proposed design

Explain the change in enough detail that the reviewer can alter the structure before code exists. Include:

- control flow and state transitions;
- files/modules to add, change, or remove;
- API, schema, event, UI, and configuration changes;
- error and recovery behavior;
- concurrency, idempotency, and compatibility;
- observability;
- security/privacy;
- performance implications.

## 5. Alternatives and rejected shortcuts

| Option | Why considered | Why chosen/rejected |
|---|---|---|
| | | |

## 6. Implementation sequence

Break work into independently verifiable steps.

| Step | Change | Evidence after step | Rollback / safety | Dependencies |
|---|---|---|---|---|
| 1 | | | | |

Avoid a plan that asks the agent to implement a large design in one run.

## 7. Test plan

| Requirement / risk | Test layer | Test oracle | Fixture / environment | Expected evidence |
|---|---|---|---|---|
| | Unit / integration / E2E / manual | | | |

## 8. Data migration and release

- Migration/backfill:
- Mixed-version compatibility:
- Feature flag / canary:
- Rollback:
- Cleanup after stable release:

## 9. Documentation and skill updates

- Requirements/design updated:
- Runbook/operational docs updated:
- Public/internal API docs updated:
- Regression lesson to add to a skill:

## 10. Review questions

- Is the change smaller than necessary or larger than necessary?
- Which business invariant can the implementation accidentally violate?
- What evidence would prove the design wrong?
- What is the first observable signal when it fails?
- Which decision still belongs to a human?

## 11. Approval

- Approved scope:
- Approved architecture/design:
- Required gates:
- Reviewer and date:
