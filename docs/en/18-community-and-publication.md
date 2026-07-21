# Community and publication strategy

## GitHub is the source of truth

Use GitHub for the public, versioned method: bilingual chapters, templates, related work, governance, and change history. Evidence-backed cases and validated real-world skills should enter later releases only when they meet the same public standard. Markdown makes every change reviewable and searchable. Word and PDF should be generated release artifacts, not the canonical source.

Use separate language files rather than placing full Chinese and English text side by side. The recommended policy is:

- Chinese is initially the source language for the long-form experience;
- English is an authored adaptation with the same facts and method;
- translation status is tied to a source commit;
- terms are maintained in a shared glossary;
- language-specific hooks may differ, but claims and evidence must not.

## LinkedIn is the discovery channel

Each LinkedIn post should explain one strong claim through one real incident and direct readers to the exact GitHub chapter or case.

Recommended first series:

1. The maintainer estimates that AI wrote more than 300,000 lines; engineering responsibility did not shrink.
2. Why AI coding still needs a complete requirements process.
3. Never let the agent start before the implementation plan is reviewed.
4. When code volume explodes, review itself must become AI-native.
5. pytest, Playwright, and Maestro as trust infrastructure.
6. Skills are engineering memory, not a prompt folder.
7. Logs are for humans and for AI retrieval.
8. Human value remains in taste, architecture, algorithms, and judgment.
9. Why repeated agent retry often enters a dead end.
10. Why lower implementation cost will make personalized software more common.

A post structure:

- a counterintuitive opening;
- a concrete project and constraint;
- the failure or cost of the common approach;
- three to five steps of the method;
- real evidence or an explicit “personal observation” label;
- limits and risks;
- a specific question inviting a counterexample;
- a deep link to the relevant GitHub page.

## Contribution design

Open contribution channels by type:

- **Case or counterexample**: context, constraint, human decision, AI work, failure, evidence, result, privacy treatment.
- **Skill**: layer, trigger, non-trigger, rules, examples, historical validation, compatibility.
- **Template**: repeated problem, real use, difference from existing templates.
- **Related work**: accurate summary, overlap, difference, and what this project should learn.
- **Translation**: source commit, glossary review, completeness, and natural language review.

Discussions are best for open questions and experience sharing. Issues should represent bounded accepted work. Pull requests should contain reviewable content changes.

## Avoiding repetition

Many public projects already cover specification-driven development, agent skills, testing, evidence gates, review, and harness engineering. Steer the Build should not claim ownership of those individual ideas.

Its distinctive contribution is the combination of:

- cross-domain practice from business, mobile, ML, voice, IoT, hardware-adjacent, and agent-service projects;
- control after code volume exceeds manual inspection;
- documentation as externalized human thinking and agent control;
- AI-native review plus independent evidence;
- observability explicitly designed for agent retrieval;
- reverse diagnosis from result to first divergence;
- defects converted into layered, governed skills;
- a concrete boundary for human taste, architecture, algorithms, technology choice, production risk, and accountability;
- the software-economic consequences of dramatically cheaper customization.

Maintain [`research/related-work.md`](../../research/related-work.md) openly. When another project covers an idea earlier or better, cite it, explain the overlap, and narrow this project's claim.

## Recommended release sequence

1. Sanitize material, add maintainer identity, confirm licenses, and make the core method easy to find.
2. Publish a methodology-first GitHub v0.1 and enable Discussions and Pages.
3. Develop evidence-rich cases, validated skills, and publication drafts locally until each is ready.
4. Convert useful discussion into bounded issues and pull requests.
5. Release later versions only when new evidence, cases, counterexamples, or validated skills justify them.
