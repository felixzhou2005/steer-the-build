# Contributing to Steer the Build

[简体中文](CONTRIBUTING.zh-CN.md)

Steer the Build welcomes practical experience, counterexamples, templates, skills, translations, and corrections. The project is evidence-oriented: a contribution becomes stronger when readers can see what was tried, what happened, how the result was measured, and where the claim stops applying.

## Before contributing

Use the channel that matches the maturity of the idea:

| Channel | Use it for |
|---|---|
| GitHub Discussions | Early ideas, open questions, experience sharing, and method debates |
| Issues | A bounded error, content gap, accepted case proposal, or concrete work item |
| Pull requests | A reviewable change with a clear scope and supporting evidence |
| Private security report | Secrets, customer data, unsafe operational instructions, or exploitable examples |

Read [SECURITY.md](SECURITY.md) before sharing logs, prompts, recordings, infrastructure details, or customer examples.

## Contributions we especially value

- A case that shows the complete path from intent to runtime evidence.
- A failure whose root cause changed a document, test, quality gate, or skill.
- A counterexample that narrows or corrects a claim in the guide.
- A reusable template that has been used in a real project.
- A skill with explicit triggers, non-triggers, exit criteria, and validation history.
- A translation reviewed by a fluent technical reader and tied to a source commit.
- A precise related-work comparison that explains overlap and difference without dismissing other projects.

## Evidence levels

Label the maturity of factual claims in a case or contribution:

| Level | Meaning |
|---|---|
| `E0 — hypothesis` | A reasoned idea that has not been tested |
| `E1 — observed` | Seen in one project or incident, with context recorded |
| `E2 — repeated` | Seen in multiple tasks or projects under stated conditions |
| `E3 — measured` | Supported by defined metrics, test artifacts, traces, or benchmarks |
| `E4 — independently reviewed` | Reproduced, challenged, or reviewed by someone other than the original author |

Personal experience is valid evidence when it is labeled as personal experience. Do not convert one observation into a universal law.

## Case-study requirements

Use [`templates/en/case-study.md`](templates/en/case-study.md). A publishable case should identify:

1. the problem, users, scope, and success criteria;
2. what was known before implementation and what changed;
3. which decisions were human-owned and which work was delegated;
4. architecture, data, UI, algorithm, or operational constraints;
5. tests, runtime evidence, and the source of the test oracle;
6. at least one failure, surprise, trade-off, or limitation;
7. the root-cause path, including the first observable divergence where possible;
8. what was added to documents, regression tests, or skills afterward;
9. facts that are withheld and why;
10. the evidence level of each major claim.

Never invent metrics, customer outcomes, quotes, screenshots, or architectural details to make a case look complete. Use an explicit `TODO`, `not measured`, or `withheld for confidentiality` marker.

## Skill requirements

Use [`templates/en/skill-spec.md`](templates/en/skill-spec.md). A skill should include:

- a narrowly defined purpose;
- positive triggers and explicit non-triggers;
- required inputs and assumptions;
- a step-by-step process;
- constraints and forbidden shortcuts;
- expected outputs and evidence;
- exit criteria;
- examples or historical failures that motivated it;
- owner, version, and review date.

A skill is not valuable merely because its prose sounds rigorous. Explain how it has been or will be tested against real tasks.

## Translation policy

Chinese and English are peer editions, not a paragraph-by-paragraph machine mirror.

- Preserve claims, uncertainty, risk boundaries, and evidence level.
- Prefer natural technical language over literal translation.
- Link a translation pull request to the source commit or source file revision used.
- Do not silently strengthen or weaken a claim during translation.
- When terminology has no stable equivalent, keep the original term once and add a short explanation.

See [`meta/translation-guide.md`](meta/translation-guide.md).

## AI-assisted contributions

AI assistance is welcome. The contributor remains responsible for accuracy, licenses, privacy, citations, and the final text.

In the pull request, disclose material AI use when it affected research, translation, case reconstruction, or generated operational instructions. A simple statement is enough, for example:

> AI assistance: used to restructure the draft and check bilingual consistency; all factual claims and sources were reviewed by the contributor.

Do not cite an AI response as evidence. Cite the underlying source, experiment, test artifact, or clearly labeled personal observation.

## Pull request workflow

1. Keep one pull request focused on one case, skill, chapter, template, or coherent correction.
2. Update both languages when the change affects a stable core claim, or mark the counterpart in [`meta/content-status.md`](meta/content-status.md) as pending translation.
3. Run the documentation checks described in [`meta/release-checklist.md`](meta/release-checklist.md).
4. Complete the pull request checklist and identify evidence level, sources, and any redactions.
5. Respond to review by changing either the claim, the evidence, or the scope. Do not resolve uncertainty through confident wording.

## Style

- Lead with the engineering problem, not the tool brand.
- Separate observation, inference, recommendation, and prediction.
- Use exact dates, versions, environments, and project conditions where they matter.
- Prefer concrete failure paths and artifacts over slogans.
- Explain boundaries and counterexamples.
- Keep tool-specific material versioned and dated because it ages faster than principles.
- Do not publish secrets, personal data, customer identifiers, private recordings, proprietary code, or security-sensitive infrastructure details.

## Licensing

By contributing, you agree that prose contributions are provided under CC BY 4.0 and reusable content under `templates/`, `skills/`, and `.github/` is provided under the MIT License, as described in [LICENSES.md](LICENSES.md). Only submit material you have the right to share.
