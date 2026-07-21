# GitHub post-creation checklist

## Create the repository

- Repository name: `steer-the-build`
- Description: `A bilingual, open field guide for human-controlled, evidence-driven AI software engineering at scale.`
- Visibility: Public
- Initialize with README: **No**
- Add `.gitignore`: **No**
- Add license through the GitHub form: **No**

The repository package already contains these files.

## Repository-specific values before the first push

- Repository username and URLs are configured for `felixzhou2005` in `CITATION.cff`, `mkdocs.yml`, and the issue template configuration
- Public maintainer identity is configured as `Felix Hui Zhou` in `CITATION.cff` and `AUTHORS.md`
- Social drafts remain local and are excluded from the public v0.1
- Optional maintainer contact in `SECURITY.md`

Before each release, review the staged public snapshot for accidental placeholders and private information. Local case evidence placeholders should remain local until real, publishable evidence is available.

## Repository settings

Enable:

- Issues
- Discussions
- Preserve this repository (optional, after the first release)
- GitHub Pages → Source: GitHub Actions

Recommended topics:

```text
ai-coding
software-engineering
coding-agents
codex
claude-code
agentic-engineering
testing
observability
ai-code-review
spec-driven-development
human-in-the-loop
bilingual
```

## Labels

Create or import these labels:

- `case-study`
- `experience-report`
- `skill-proposal`
- `content-gap`
- `related-work`
- `translation`
- `evidence-needed`
- `security`
- `good-first-contribution`
- `counterexample`

## Branch protection for `main`

Recommended minimum:

- require a pull request before merging;
- require the documentation quality workflow;
- require conversation resolution;
- block force pushes and deletion;
- require signed commits only when all maintainers can support it;
- keep an administrator escape path for the first setup, then tighten it.

## First release

- Tag: `v0.1.0`
- Title: `Steer the Build v0.1 — Initial field guide`
- Attach the Word master only as an optional release artifact; Markdown remains the source of truth.
- State clearly that project-specific case evidence is still being added.
- Create a GitHub Discussion asking contributors for cases and counterexamples.

## Social preview

After the repository is live, create a 1280×640 social preview containing only:

- Steer the Build
- AI builds. Humans steer. Evidence decides.
- Human-Controlled, Evidence-Driven AI Software Engineering

Avoid model logos so the project remains tool-agnostic.
