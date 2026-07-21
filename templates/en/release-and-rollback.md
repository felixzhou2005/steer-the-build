# Release and rollback plan

> Release:  
> Release owner:  
> Target date:  
> Risk: Low / Medium / High / Critical  
> Change window:

## 1. Scope and evidence

- Included changes:
- Excluded changes:
- Requirement/test/review evidence:
- Known limitations:
- Security/privacy approval:
- Performance evidence:

## 2. Dependencies and compatibility

- Minimum/maximum compatible versions:
- Database/schema compatibility:
- Client/mobile/device rollout lag:
- External systems:
- Feature flags and configuration:

## 3. Pre-release checklist

- [ ] Build artifacts are reproducible and identified.
- [ ] Required tests and AI review passed.
- [ ] Migrations/backfills were rehearsed on representative data.
- [ ] Backup and restore were verified when required.
- [ ] Dashboards, alerts, and runbooks are ready.
- [ ] Rollback authority and communication channel are assigned.
- [ ] Customer/support/operations communication is prepared.
- [ ] Production commands have human review and least privilege.

## 4. Rollout stages

| Stage | Population / traffic | Duration | Entry criteria | Health signals | Stop condition |
|---|---:|---:|---|---|---|
| Internal / shadow | | | | | |
| Canary | | | | | |
| Partial | | | | | |
| Full | | | | | |

## 5. Migration and backfill

- Sequence:
- Rate limits and load impact:
- Validation queries:
- Mixed-version behavior:
- Restart/resume behavior:
- Data correction plan:

## 6. Rollback or roll-forward

- Decision threshold:
- Responsible approver:
- Code rollback:
- Configuration/feature flag rollback:
- Schema/data rollback or compensating action:
- Client/device version constraints:
- Verification after rollback:

A rollback plan that cannot reverse data or external side effects must say so and define compensation.

## 7. Observability window

- Release markers and version tags:
- Metrics/logs/traces to watch:
- Business and safety outcomes:
- Monitoring duration:
- On-call handoff:

## 8. Post-release

- Acceptance confirmation:
- Cleanup of flags/dual paths:
- Documentation and skill updates:
- Incident or near-miss review:
- Final release record:
