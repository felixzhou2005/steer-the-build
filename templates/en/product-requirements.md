# Product requirements document

> Product / feature:  
> Owner:  
> Status: Discovery / Draft / Approved / Shipped  
> Version:  
> Last updated:

## 1. Executive summary

Describe the user or business problem, the intended outcome, and why it matters now in five sentences or fewer.

## 2. Problem evidence

- Who experiences the problem?
- What do they do today?
- What pain, delay, error, cost, or missed opportunity exists?
- What evidence supports the problem: interviews, logs, tickets, metrics, contracts, or direct observation?
- What remains an assumption?

## 3. Users and context

| User / actor | Goal | Context | Current workaround | Consequence of failure |
|---|---|---|---|---|
| | | | | |

Include administrators, operators, external systems, devices, and support staff—not only the primary end user.

## 4. Outcomes and success measures

| Outcome | Baseline | Target | Measurement method | Review window |
|---|---:|---:|---|---|
| | | | | |

Separate product value metrics from implementation throughput. Lines of code, agent tokens, and number of generated files are not product outcomes.

## 5. Scope

### In scope

- 

### Explicit non-goals

- 

### Future possibilities that must not influence the current design

- 

## 6. User journeys

For each critical journey, write:

- trigger;
- preconditions;
- happy path;
- alternate path;
- failure path;
- recovery or human handoff;
- observable completion state.

## 7. Functional requirements

Use stable identifiers so requirements can be mapped to design, tests, and release evidence.

| ID | Requirement | Priority | Acceptance evidence | Owner |
|---|---|---|---|---|
| FR-001 | | Must / Should / Could | | |

Avoid words such as “fast,” “intuitive,” “secure,” “smart,” or “accurate” unless a measurable definition follows.

## 8. Business rules and invariants

List rules that must remain true across UI, API, database, jobs, and failure recovery.

| ID | Invariant | Where enforced | Failure consequence |
|---|---|---|---|
| BR-001 | | | |

## 9. Data and AI behavior

- Inputs and their provenance:
- Outputs and who may rely on them:
- Required explanations or confidence:
- Human override and appeal:
- Unacceptable behavior or content:
- Retention and deletion expectations:
- Model or automation fallbacks:

## 10. Edge cases and exception inventory

| Scenario | Expected behavior | User communication | Evidence needed |
|---|---|---|---|
| | | | |

## 11. Dependencies and constraints

- Legal, privacy, security, contractual, localization, accessibility:
- Platform, device, browser, hardware, or network constraints:
- External systems and ownership:
- Budget, schedule, staffing, and operational constraints:

## 12. Risks and open decisions

| Item | Type | Impact | Owner | Decision date / mitigation |
|---|---|---|---|---|
| | Risk / assumption / question | | | |

## 13. Acceptance map

Link each must-have requirement to at least one independent evidence source.

| Requirement | Test / evidence | Environment | Result owner |
|---|---|---|---|
| FR-001 | | | |

## 14. Approval

- Product owner:
- Engineering / architecture owner:
- Security / privacy owner when required:
- Operations owner when required:
- Approval date and version:
