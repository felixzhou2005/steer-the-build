# Database design

> System / bounded context:  
> Data owner:  
> Status: Proposed / Approved / Implemented  
> Database / version:  
> Related architecture:

## 1. Data purpose and ownership

- Business capabilities supported:
- Source of truth for each entity:
- Writers and readers:
- Data classification and retention:
- Explicitly derived, cached, denormalized, or analytical data:

## 2. Access patterns first

| ID | Operation | Frequency / peak | Filter and sort | Rows / payload | Latency target | Consistency need |
|---|---|---:|---|---:|---:|---|
| AP-001 | | | | | | |

Schema and index choices must be justified against actual access patterns, not generic normalization or generic NoSQL advice.

## 3. Entity and table design

For each table/collection:

- business meaning;
- owner;
- primary key and identifier semantics;
- column/field type, unit, nullability, default, and semantic comment;
- constraints and invariants;
- lifecycle and deletion behavior;
- expected size and growth;
- sensitive fields;
- generated or redundant fields and their update rule.

## 4. Relationships and consistency

- Transaction boundaries:
- Referential integrity:
- Cross-service or cross-store consistency:
- Event/outbox strategy:
- Conflict and duplicate handling:
- Read model / wide table / denormalization rationale:

Denormalization is a deliberate performance trade-off. Document how redundant values remain correct and how drift is detected.

## 5. Indexes and query design

| Query / access pattern | Index | Expected plan | Write cost | Evidence |
|---|---|---|---|---|
| | | | | |

Require `EXPLAIN`/query-plan evidence for critical SQL. Prefer simple, explicit queries that satisfy measured needs; do not add complex fallback logic without a requirement.

## 6. Partitioning, retention, and archival

- Partition key and skew risk:
- Hot-key/hot-partition mitigation:
- TTL / retention:
- Archive and restore:
- Legal hold and deletion:

## 7. Migration plan

- Forward schema change:
- Backfill strategy and rate limit:
- Dual-read/write period:
- Compatibility window:
- Validation queries:
- Rollback or roll-forward:
- Backup and restore test:

## 8. Security and privacy

- Database roles and least privilege:
- Encryption and key ownership:
- Row/tenant isolation:
- Audit and access review:
- Masking in lower environments:
- Logging restrictions:

## 9. Performance and capacity evidence

- Representative dataset:
- Baseline queries and plans:
- Load/concurrency test:
- Storage and index growth:
- Maintenance tasks:
- Alert thresholds:

## 10. Review checklist

- [ ] Every field has a stable business meaning.
- [ ] Constraints enforce important invariants.
- [ ] Critical access patterns have query-plan evidence.
- [ ] Redundancy has a consistency mechanism.
- [ ] Migration and rollback are tested.
- [ ] Privacy, retention, and deletion are explicit.
- [ ] Observability can identify slow or failing operations.
