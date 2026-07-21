# Observability specification

> System / flow:  
> Owner:  
> Status: Draft / Approved / Implemented  
> Data classification:  
> Retention:

The objective is not maximum log volume. It is enough structured, correlated, privacy-safe evidence to understand behavior and locate the first divergence quickly.

## 1. Diagnostic questions

List the questions an operator or AI agent must be able to answer, for example:

- Which user/tenant/device/job/model version was affected?
- Which stage first departed from expected behavior?
- Was the failure caused by input, state, dependency, model, code, configuration, or deployment?
- What retried, degraded, or partially succeeded?
- Can the exact request or decision be reproduced safely?

## 2. Critical flow map

| Stage | Input | Decision / state change | Dependency | Output | Failure signal |
|---|---|---|---|---|---|
| | | | | | |

## 3. Correlation model

Define identifiers and propagation rules:

- `trace_id` / `span_id`;
- `request_id` / `session_id` / `job_id`;
- anonymized `user_id`, `tenant_id`, `device_id`;
- order/transaction/entity ID;
- deployment, configuration, model, prompt, and skill versions.

Do not use raw personal identifiers when a stable pseudonymous key is sufficient.

## 4. Structured events

| Event name | When emitted | Required fields | Severity | Sampling |
|---|---|---|---|---|
| | | | | |

Prefer stable event names and typed fields over free-form prose. Record before/after state only when safe and necessary.

## 5. Metrics and SLOs

| Metric | Type | Labels with bounded cardinality | Objective / threshold | Action |
|---|---|---|---|---|
| | Counter/gauge/histogram | | | |

## 6. Traces

- Trace boundaries and sampling:
- Required spans for external calls, model inference, database, queue, device, and critical decisions:
- Attributes and status mapping:
- Links across asynchronous work:
- Trace-to-log and trace-to-metric navigation:

## 7. AI/ML-specific evidence

- model/provider/version;
- prompt/template and skill version;
- input/output classification and safe hash/reference;
- token, latency, retry, fallback, confidence, and moderation outcome;
- tool calls and authorization decision;
- evaluation or feedback linkage.

Never log full sensitive prompts or recordings by default.

## 8. Privacy and security

- Prohibited fields:
- Redaction at source:
- Access control:
- Retention and deletion:
- Audit of diagnostic access:
- Safe lower-environment fixtures:

## 9. Dashboards and alerts

For each alert, define user impact, signal, threshold, time window, owner, runbook, and anti-noise rule. Alerts should identify a decision or action, not merely state that a metric changed.

## 10. Failure artifact bundle

Define the minimal bundle an AI diagnosis session receives:

- failing input or safe reference;
- exact versions and feature flags;
- correlated logs/traces/metrics window;
- expected vs actual stage outputs;
- recent deployments or migrations;
- reproduction command/environment;
- privacy classification.

## 11. Verification

Inject representative failures and confirm that a reviewer who did not write the code can identify the first divergence within the target diagnosis time.
