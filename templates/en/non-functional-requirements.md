# Non-functional requirements

> System / feature:  
> Owner:  
> Status: Draft / Approved  
> Measurement environment:  
> Last reviewed:

Non-functional requirements must be measurable enough to become architecture constraints, test plans, dashboards, and release gates.

## 1. Workload model

- Active users, tenants, devices, jobs, or concurrent sessions:
- Typical and peak request rate:
- Data volume and growth:
- Request/response or media sizes:
- Geographic and network conditions:
- Burst behavior and scheduled workloads:

## 2. Performance budgets

| Flow / operation | Metric | Target | Worst acceptable | Measurement environment |
|---|---|---:|---:|---|
| | p50 / p95 / p99 / throughput | | | |

Include end-to-end latency, not only server execution time. For voice or IoT, define capture-to-response and command-to-device latency.

## 3. Reliability and recovery

- Availability objective:
- Error-rate objective:
- Data durability objective:
- Recovery time objective (RTO):
- Recovery point objective (RPO):
- Degraded mode:
- Retry and idempotency policy:
- Backup verification schedule:

## 4. Scalability and capacity

- Scaling unit and bottleneck hypothesis:
- Hard limits and quotas:
- Capacity alert thresholds:
- Load-test model:
- Expected behavior when limits are reached:

## 5. Security

- Authentication and session requirements:
- Authorization model and tenant boundaries:
- Secrets and key management:
- Encryption requirements:
- Audit events:
- Dependency and supply-chain controls:
- Destructive-operation approval:

## 6. Privacy and data governance

- Personal or sensitive data categories:
- Purpose and lawful/contractual basis:
- Data minimization:
- Retention and deletion:
- Redaction in logs, prompts, traces, and test fixtures:
- Data residency and subprocessors:
- User access, correction, and deletion workflows:

## 7. Safety and human control

For systems that affect physical devices, money, orders, communications, or high-impact decisions:

- commands requiring confirmation;
- safe default and emergency stop;
- human handoff and override;
- rate, scope, and authority limits;
- behavior under uncertain intent or model confidence;
- audit and replay requirements.

## 8. Accessibility and localization

- Accessibility standard and tested assistive technologies:
- Keyboard, screen reader, contrast, motion, caption, and text-scaling requirements:
- Supported languages, locales, time zones, number/currency/date formats:
- Content and UI expansion tolerance:

## 9. Compatibility

- Supported OS, browser, device, hardware, and protocol versions:
- Backward/forward compatibility window:
- API and schema deprecation policy:
- Offline or intermittent-network behavior:

## 10. Operability and observability

- Required logs, metrics, traces, dashboards, and alerts:
- Correlation identifiers:
- Diagnostic retention:
- On-call and escalation expectations:
- Runbooks and recovery drills:

## 11. Maintainability

- Maximum acceptable complexity or module size where applicable:
- Required static checks and documentation:
- Upgrade cadence and ownership:
- Test execution budget:
- Bus-factor or knowledge-transfer requirements:

## 12. Cost and resource budgets

| Resource | Unit | Typical budget | Peak budget | Alert / stop condition |
|---|---|---:|---:|---|
| Model tokens / inference | | | | |
| Compute / storage / network | | | | |
| External API | | | | |
| Human operations | | | | |

## 13. Verification matrix

| NFR ID | Requirement | Test or telemetry | Frequency | Release gate? |
|---|---|---|---|---|
| NFR-001 | | | | Yes / No |
