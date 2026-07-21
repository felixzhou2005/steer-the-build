# API design

> API / service:  
> Owner:  
> Status: Proposed / Approved / Implemented  
> Versioning policy:  
> Related requirements:

## 1. Purpose and consumers

- Business capability:
- Consumers and trust level:
- Synchronous/asynchronous rationale:
- Explicit non-goals:

## 2. Domain semantics

Define terms, identifiers, state machines, ownership, and invariants before listing endpoints. Avoid using the same field name for different business meanings.

## 3. Contract inventory

| Operation / event | Consumer | Authorization | Idempotent? | Latency / delivery objective | Owner |
|---|---|---|---|---|---|
| | | | | | |

## 4. Request and response schema

For every operation include:

- method, path/topic, and version;
- authentication and authorization rule;
- field name, type, unit, nullability, default, validation, and semantic description;
- examples for normal, boundary, and invalid input;
- response and error schema;
- pagination, filtering, sorting, and limits;
- correlation and idempotency keys;
- privacy classification.

## 5. Error model

| Error code | Meaning | Retryable? | Client action | Logged evidence |
|---|---|---|---|---|
| | | | | |

Do not collapse business rejection, authentication failure, validation failure, dependency outage, and internal error into one ambiguous response.

## 6. Idempotency, concurrency, and consistency

- Duplicate request behavior:
- Optimistic or pessimistic concurrency:
- Ordering guarantees:
- Partial failure behavior:
- Read-after-write expectation:
- Event deduplication and replay:

## 7. Security and abuse resistance

- Object-level authorization:
- Tenant isolation:
- Input and output filtering:
- Rate and cost limits:
- Sensitive fields and redaction:
- Webhook/event verification:
- AI or tool-invocation authorization:

## 8. Compatibility and lifecycle

- Breaking-change definition:
- Additive-change rules:
- Deprecation notice and window:
- Consumer contract tests:
- Schema registry or generated clients:
- Rollback compatibility:

## 9. Observability

- Operation name and trace attributes:
- Request/result metrics:
- Safe structured logs:
- SLO and alert thresholds:
- Audit events:

## 10. Verification

Link contract tests, integration tests, negative tests, performance tests, authorization tests, and example fixtures. State which evidence is independent of the implementation.
