# Incident analysis

> Incident ID:  
> Date/time and timezone:  
> Severity:  
> Incident lead:  
> Status: Draft / Reviewed / Closed

The purpose is to understand and improve the system, not to assign blame. Distinguish triggering event, contributing conditions, detection gaps, response decisions, and systemic root causes.

## 1. Summary

In plain language: what happened, who or what was affected, duration, and current status.

## 2. Impact

- Users/tenants/devices/orders affected:
- Incorrect or delayed outcomes:
- Data, privacy, security, financial, or physical impact:
- Scope confidence and unknowns:

## 3. Timeline

Use exact timestamps and distinguish event time from discovery time.

| Time | Event / evidence | Decision / action | Actor |
|---|---|---|---|
| | | | Human / AI / system |

## 4. Expected vs actual flow

Map the critical stages and identify the **first observable divergence**, not only the final symptom.

| Stage | Expected | Actual | Evidence |
|---|---|---|---|
| | | | |

## 5. Detection and response

- How was it detected?
- Which signal should have detected it earlier?
- What evidence was missing or too noisy?
- What did the responding AI/human try?
- Were there circular retries or theme drift?
- How was impact contained and service restored?

## 6. Root-cause analysis

### Trigger

- 

### Technical root cause

- 

### Systemic and process contributors

- Missing or ambiguous requirement:
- Architecture/design gap:
- Test-oracle or coverage gap:
- Review gap:
- Observability gap:
- Skill/rule gap:
- Release/operations gap:

Avoid ending at “the AI wrote bad code” or “human error.” Explain why the control system allowed the failure.

## 7. Counterfactuals

Which single earlier signal, decision, test, or constraint would have prevented or sharply reduced the incident?

## 8. Corrective actions

| Action | Type | Owner | Due | Verification | Status |
|---|---|---|---|---|---|
| | Code / test / document / skill / architecture / operations | | | | |

Prioritize controls that prevent the class of failure, not only the exact input.

## 9. Lessons converted to durable assets

- Regression tests:
- Requirement/design changes:
- New or updated Skill:
- Dashboard/alert/runbook changes:
- Training or review changes:

## 10. Evidence and disclosure

- Logs/traces/test artifacts retained:
- Sensitive details redacted:
- Evidence level of conclusions:
- Public summary and withheld facts:
