# Source review policy

## Purpose

External sources are used to verify changing facts, define established terminology, compare related work, and avoid presenting common ideas as unique. The field guide's practical claims should remain clearly separated from externally verified facts.

## Source priority

Use the strongest available source for each type of claim:

1. official standards, specifications, or government publications;
2. official project documentation and repositories;
3. original research papers or first-party engineering reports;
4. reputable independent engineering analysis;
5. community discussions only as examples of practice or disagreement.

## Rules

- Record the source title, canonical link, access date, and the exact claim it supports.
- Prefer primary sources for technical behavior and security guidance.
- State when a comparison is an inference rather than a source's own conclusion.
- Do not cite a tool vendor's marketing claim as independent proof of quality.
- Do not copy long passages. Summarize and link.
- Recheck facts that can change, including tool versions, security models, licensing, and platform behavior.
- Represent disagreement when reputable sources materially conflict.
- Never use an external source to fill in unknown facts about the maintainer's private projects.

## Review cadence

Before each tagged release:

- check all external links;
- review sources marked as version-sensitive;
- inspect related work added since the previous release;
- confirm that differentiation language remains accurate;
- update `CHANGELOG.md` when a source materially changes a recommendation.

## Adding a source

A pull request should explain:

- the claim being supported;
- why this source is authoritative enough;
- the relevant page or section;
- whether the source is stable or requires periodic review;
- which English and Chinese pages need synchronized changes.
