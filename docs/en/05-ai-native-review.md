# AI-native review

## Why review must change

When an agent generates hundreds of thousands of lines, exhaustive human line-by-line review is not a credible primary control. The response is not to eliminate review. It is to redesign review around architecture, behavior, risk, evidence, and targeted inspection.

A precise statement is:

> At large AI-generated code volume, manual line-by-line review cannot remain the primary quality mechanism. AI-assisted, evidence-based, risk-weighted review becomes primary; deep human review remains mandatory for high-risk decisions and paths.

## Review layers

### 1. Architecture review

Ask whether the change:

- respects module and dependency boundaries;
- preserves approved invariants and data ownership;
- introduces unnecessary abstraction or dependencies;
- changes failure domains, deployment, or tenancy;
- creates coupling that will make later changes harder;
- conflicts with ADRs or documented architecture.

### 2. Functional review

Trace requirements to behavior:

- Are all stated scenarios implemented?
- Are alternate and error paths covered?
- Are permissions and state transitions correct?
- Did the implementation quietly change the meaning of acceptance criteria?
- Which requirements have no supporting test or runtime evidence?

### 3. Implementation review

Inspect details that commonly hide defects:

- concurrency, race conditions, idempotency, retries, and partial failure;
- SQL complexity, query plans, N+1 access, and transaction boundaries;
- input validation, authorization, secrets, and sensitive logging;
- resource lifetime, memory, network, and cache behavior;
- exception handling that suppresses failure;
- duplicated logic, dead paths, and accidental fallback expansion.

### 4. Evidence review

Review the proof, not only the diff:

- Do tests use an independent oracle?
- Were tests added before or after implementation, and can they fail for the right reason?
- Are traces, screenshots, recordings, benchmarks, or hardware results available?
- Were migrations and rollback tested in a disposable environment?
- Are claims bound to the exact source version under review?

## Avoid self-certification

A single agent can implement a mistaken interpretation, generate tests based on the same interpretation, run them successfully, and declare completion. That is a self-proof loop, not independent validation.

Reduce this risk by deriving test oracles from sources independent of the implementation:

- approved requirements and business invariants;
- historical production examples;
- golden datasets;
- a previous trusted implementation;
- differential and property testing;
- a separate reviewer agent with a clean context;
- real browser, device, service, or hardware execution;
- human acceptance for subjective product qualities.

## A recommended review workflow

1. Freeze the reviewed requirement, plan, and source revision.
2. Ask an independent reviewer agent to summarize the change without using the implementer's narrative as truth.
3. Run architecture, functional, implementation, security, performance, and evidence review passes separately.
4. Convert findings into severity, affected invariant, evidence, and remediation.
5. Reject vague findings that cannot identify a path, condition, or unsupported claim.
6. Re-run the relevant tests and review after remediation.
7. Require human approval for high-risk findings, exceptions, and release.

A review report should include:

- reviewed commit or diff;
- source requirements and plan;
- assumptions and missing context;
- findings by severity;
- affected files and runtime paths;
- evidence supporting each finding;
- unverified areas;
- human decisions and accepted residual risk.

## What humans still inspect deeply

Human deep review should be concentrated where errors are expensive, irreversible, or difficult to observe:

- business invariants and money movement;
- authentication and authorization boundaries;
- destructive operations and data migrations;
- public contracts and compatibility;
- algorithmic core and evaluation logic;
- concurrency and distributed state;
- safety-relevant IoT or hardware commands;
- multi-tenant isolation and secrets;
- production automation and rollback;
- visual identity and product judgment.

The human is no longer the person manually correcting every line. The human defines the review questions, decides which evidence counts, identifies the highest-risk paths, challenges assumptions, and owns the decision to ship.
