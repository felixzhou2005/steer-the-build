# Case-study strategy

Project descriptions should be included. Without cases, the method can sound like a polished restatement of standard software engineering. Cases show how the same controls behave differently in ML, mobile, voice, IoT, business transactions, and agent services.

## Cases are evidence, not a portfolio list

Do not write only “I built a home valuation model” or “I deployed OpenClaw as a service.” A useful case explains:

1. the business problem and success criteria;
2. the highest-risk uncertainty;
3. documents created from requirement to operation;
4. decisions retained by the human and why;
5. work delegated to AI;
6. architecture and implementation boundaries;
7. test tools and independent oracles;
8. observability and diagnostic design;
9. a significant failure or surprising result;
10. reverse diagnosis from output to root cause;
11. the test, document, template, or skill created afterward;
12. measured time, quality, cost, or business outcome;
13. what cannot be disclosed and why.

## Recommended first deep cases

### Home valuation

Demonstrate human control of algorithmic framing, data validity, baseline, metrics, outliers, geographic/time scope, uncertainty, and reverse analysis of implausible outputs.

### iOS application

Demonstrate Figma control, AI implementation, visual fidelity, state and device coverage, Maestro flows, performance, and release quality.

### IoT voice and remote control

Demonstrate boundaries among device, network, backend, AI, authorization, offline state, replay protection, audit, and physical safety.

### AI receptionist with order synchronization

Demonstrate voice pipeline observability, consent, intent and confirmation, business transaction consistency, human handoff, and recovery from partial failure.

### OpenClaw cloud deployment / as a service

Demonstrate skill governance, scheduling, observability, isolation, credentials, tenant model, update policy, and AI-assisted operations.

## Short cases to add next

- automated posting;
- content collection, AI judgment, and sales lead formation;
- scheduled OpenClaw skills such as monitoring review volume;
- real-time phone translation;
- AI debate coaching.

These can begin as one-page cases and become deep cases when sanitized metrics, failures, and evidence are available.

## Public-safety review

Before publishing:

- remove customer names, secrets, raw calls, personal data, internal URLs, and proprietary code;
- confirm data collection and platform terms for scraping, posting, and lead generation;
- describe consent, retention, and redaction for calls and translations;
- omit device commands or infrastructure details that enable abuse;
- state limits and uncertainty for valuation or ML outputs;
- explain isolation and permissions for OpenClaw service scenarios;
- distinguish measured results from personal judgment;
- obtain authorization for third-party screenshots or data.

Each case directory in this repository is prefilled with known context and explicit evidence gaps so that missing facts are visible rather than invented.
