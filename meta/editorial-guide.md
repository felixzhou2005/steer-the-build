# Editorial guide

## Voice

Write as an experienced practitioner documenting a method, not as a vendor promising autonomy. Prefer concrete mechanisms, evidence, trade-offs, and failure conditions over superlatives.

## Claim levels

Label claims by their basis:

- **Observed in this practice:** a first-person observation from one or more projects.
- **Proposed method:** a recommendation that may still need broader validation.
- **Externally verified fact:** supported by an authoritative source.
- **Hypothesis:** a prediction or interpretation to be tested.

Do not silently convert an observation into a universal law.

## Required structure for a method chapter

1. problem or failure pattern;
2. principle;
3. operating procedure;
4. evidence and completion criteria;
5. boundary and counterexample;
6. related template, skill, or case;
7. open questions.

## Required structure for a case

Use [the case-study template](../templates/en/case-study.md). Every case should separate:

- known facts;
- interpretation;
- measured results;
- estimates;
- information intentionally withheld;
- information not yet collected.

## Terminology

Use the definitions in [the glossary](../research/glossary.md). Prefer “AI coding agent” or “agent” over anthropomorphic language when the distinction matters. “Human-in-control” means retained authority and accountability, not constant manual intervention.

## Numbers

- Give units, time periods, and denominators.
- Explain how a metric was collected.
- Mark estimates as estimates.
- Do not use generated code lines as a quality measure.
- Do not publish private operational numbers without authorization.

## Sensitive material

Remove secrets, personal data, customer identifiers, private endpoints, exact infrastructure weaknesses, proprietary samples, and attack-enabling detail. Preserve the engineering lesson through abstraction or a synthetic example clearly labeled as such.
