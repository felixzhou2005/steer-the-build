# Performance, release, and AI-assisted DevOps

## Performance must be governed by evidence

AI-generated code often prioritizes completeness and apparent robustness over simplicity and cost. Common patterns include:

- SQL with unnecessary joins, nested queries, defensive conditions, or repeated scans;
- duplicate serialization, conversion, copying, or network calls;
- abstractions introduced for hypothetical future use;
- excessive retries and fallbacks;
- caches without a measured need or invalidation design;
- mobile work on the main thread, excessive renders, or battery-intensive polling;
- ML pipelines with avoidable preprocessing or inference overhead.

The answer is not “tell the agent to optimize.” Establish budgets and measure.

## Performance governance loop

1. Define workload and target environment.
2. Set explicit budgets: latency percentiles, throughput, memory, storage, network, battery, cold start, query count, inference cost, or device timing.
3. Record a baseline before the change.
4. Profile or trace the actual bottleneck.
5. Ask the agent for the simplest change that addresses measured evidence.
6. Benchmark before and after with equivalent input.
7. Test correctness and stability after optimization.
8. Record the result and prevent regression.

A SQL skill should require simple, readable, index-aware queries; prohibit speculative fallback logic; require an explanation of access paths and cardinality; and ask for `EXPLAIN` or equivalent evidence when performance matters.

## Release is part of implementation

A feature is not complete when it works in a developer environment. The plan must include:

- configuration and secret changes;
- backward compatibility;
- database or data migration;
- deployment order across services and clients;
- feature flags or staged exposure;
- monitoring and alert thresholds;
- rollback and data recovery;
- ownership and incident response;
- removal of temporary compatibility paths.

Migrations should be exercised against realistic data in a disposable environment. Rollback must be tested, not assumed. For irreversible transformations, use backups, shadow writes, verification queries, and explicit human approval.

## AI can be a strong development operations engineer

Coding agents are effective at Linux commands, environment setup, build scripts, containers, deployment manifests, log inspection, and repetitive diagnosis. They can substantially reduce the historical friction between development and operations, especially in infrastructure-heavy projects.

Use high autonomy in local and disposable test environments, where the agent can:

- install and configure dependencies;
- build and run services;
- inspect processes, ports, files, and logs;
- create repeatable scripts;
- test deployment and recovery procedures;
- compare environment state with documentation.

## Production remains controlled

Do not give an agent unrestricted production authority merely because its commands worked in development.

Production controls should include:

- least-privilege, time-bounded credentials;
- read-only diagnosis by default;
- reviewed and versioned scripts rather than ad hoc command generation;
- dry-run or plan output where available;
- explicit approval for destructive or irreversible actions;
- backups and verified rollback;
- audit logs and command capture;
- blast-radius limits, canaries, and staged rollout;
- separation of duties for critical systems;
- an immediate human stop path.

The desired pattern is: let AI develop, test, and explain the operation; turn it into a deterministic script or runbook; validate it in a representative environment; then execute production changes through the normal risk gate.
