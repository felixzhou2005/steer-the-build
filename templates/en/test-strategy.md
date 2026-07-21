# Test strategy

> System / release:  
> Test owner:  
> Status: Draft / Approved / Executed  
> Risk classification:  
> Last updated:

## 1. Quality risks

Rank failures by consequence and likelihood. Examples include wrong business decisions, data loss, unauthorized action, order inconsistency, UI state omission, model drift, device command error, and operational rollback failure.

| Risk | Consequence | Likelihood | Detection layer | Release-blocking? |
|---|---|---|---|---|
| | | | | |

## 2. Test oracle

For each important behavior, define where expected results come from:

- approved requirement or invariant;
- contract or protocol specification;
- curated/golden examples;
- previous trusted implementation;
- differential or metamorphic relationship;
- domain expert judgment;
- device, browser, or real-world observation.

Avoid allowing the same agent to invent the implementation, expected result, and passing test from one unreviewed assumption.

## 3. Test layers

| Layer | Scope | Tool/examples | Owner | When run |
|---|---|---|---|---|
| Static | Types, lint, dependency, security | | | |
| Unit | Pure logic and invariants | pytest, platform framework | | |
| Component | Module/UI component behavior | | | |
| Integration | Database, queue, model, device, external API | | | |
| Contract | Consumer/provider and schema compatibility | | | |
| End-to-end | Critical user/business journey | Playwright, Maestro | | |
| Non-functional | Load, resilience, accessibility, security | | | |
| Exploratory/human | Taste, ambiguity, novel behavior | | | |

Tools are examples, not evidence by themselves. Record exact versions and environments.

## 4. Requirement-to-evidence matrix

| Requirement / invariant | Unit | Integration | E2E | Runtime signal | Human review |
|---|---|---|---|---|---|
| | | | | | |

## 5. Test data

- Synthetic, anonymized, or production-derived source:
- Privacy and retention:
- Golden dataset ownership:
- Boundary and adversarial cases:
- Temporal/version stability:
- Reset and isolation strategy:

## 6. Environment matrix

Include browser, OS, device, hardware, network, locale, data scale, service versions, model versions, and feature flags that can change behavior.

## 7. Failure-path coverage

- dependency timeout/outage;
- duplicate, reordered, or partial messages;
- permission denial;
- invalid, missing, stale, or extreme data;
- retry and cancellation;
- offline/intermittent network;
- rollback and mixed versions;
- model uncertainty, abstention, or malformed output;
- device unavailable or unsafe command.

## 8. AI-driven test execution

Define which agents may generate tests, run tools, inspect failures, and propose fixes. Require preservation of failing artifacts and limit blind fix/retry loops. A failing test may reveal a test defect, requirement conflict, environment defect, or product defect; classify before changing code.

## 9. Quality gates

| Gate | Threshold | Evidence | Exception authority |
|---|---|---|---|
| | | | |

## 10. Reporting

- Test report location:
- Screenshots/videos/traces:
- Flake tracking:
- Coverage interpretation:
- Known untested areas:
- Release recommendation:
