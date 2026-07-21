# Checks by project type

The same lifecycle applies across projects, but evidence and failure modes differ.

## Business systems

Focus on:

- exact business rules and terminology;
- roles, permissions, tenant and data ownership;
- money, order, inventory, and state-machine invariants;
- idempotency and external-system synchronization;
- audit history, retention, and customer support paths;
- migration and backward compatibility;
- realistic end-to-end workflows and exception cases.

A common danger is a functionally complete interface backed by subtly wrong state or authorization logic.

## Mobile applications

Focus on:

- Figma fidelity and visual regression;
- navigation and state restoration;
- offline, poor-network, background, and interruption behavior;
- permissions, privacy prompts, deep links, push notifications;
- device, OS, locale, orientation, accessibility, and screen-size matrix;
- battery, memory, launch time, and main-thread work;
- Maestro or equivalent real-flow automation plus selected physical-device tests;
- app-store packaging, migration, and rollout.

## Pure technical or infrastructure projects

Focus on:

- API and command contracts;
- portability and supported environments;
- resource usage and performance baselines;
- deterministic builds and dependency control;
- failure recovery, idempotency, and cleanup;
- security boundaries and least privilege;
- reproducible examples and operational documentation.

Agents often over-generalize infrastructure code. Keep the supported scope explicit.

## Hardware, embedded, and IoT

Focus on:

- hardware/software responsibility boundaries;
- timing, power, memory, network, and environmental constraints;
- device identity, secure provisioning, command authorization, and replay protection;
- offline behavior and eventual state reconciliation;
- safe defaults, watchdogs, physical emergency stop, and failure containment;
- simulator, protocol, hardware-in-the-loop, and real-device evidence;
- firmware compatibility, staged rollout, and recovery from interruption;
- complete audit of voice or remote commands.

No AI-generated command should be allowed to create physical danger without deterministic safety layers.

## Machine learning

Focus on:

- problem and target definition;
- data source, rights, lineage, leakage, bias, and time/geography validity;
- simple baseline before a complex model;
- train/validation/test split and experiment reproducibility;
- metrics tied to real error cost;
- calibration, uncertainty, outliers, sparse segments, and drift;
- model, feature, data, and prompt versioning;
- latency and inference cost;
- human review and fallback;
- post-deployment monitoring and retraining criteria.

AI can propose many sophisticated models. A model should win by valid evidence, not by novelty.

## Voice and phone systems

Focus on:

- consent and disclosure;
- audio quality, segmentation, latency, interruption, and turn-taking;
- ASR, language detection, translation, intent, and action as separately observable stages;
- sensitive data redaction and retention;
- confirmation for orders, money, addresses, and irreversible actions;
- human handoff and failure messaging;
- synchronization with the business backend;
- evaluation across accents, noise, language pairs, and edge cases.

## OpenClaw and agent services

Focus on:

- treating skills and plugins as code;
- source review, versioning, allowlists, and emergency revocation;
- tenant, process, filesystem, credential, session, and network isolation;
- least privilege and task-specific credentials;
- scheduled-job ownership, budgets, retries, and audit;
- prompt injection and untrusted content boundaries;
- observability of tool calls and side effects;
- whether the trust model is single-operator or truly multi-tenant.

A service offering should not assume that a personal-assistant trust model automatically provides adversarial tenant isolation.
