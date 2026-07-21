# Repository structure

```text
steer-the-build/
├── README.md / README.zh-CN.md       # Public landing pages
├── QUICKSTART.md / QUICKSTART.zh-CN.md
├── docs/
│   ├── en/                           # 20 English method chapters
│   └── zh-CN/                        # 20 Chinese chapters + full-book edition
├── templates/
│   ├── en/                           # 20 operational templates
│   └── zh-CN/                        # 20 corresponding Chinese templates
├── research/                         # Related work, differentiation, glossary
├── meta/                             # Maintainer, editorial, translation, release guides
├── scripts/                          # Link, bilingual, and site-build validation
├── .github/
│   ├── ISSUE_TEMPLATE/               # Evidence-oriented contribution forms
│   └── workflows/                    # Quality checks and GitHub Pages deployment
├── mkdocs.yml                        # Documentation website configuration
├── requirements-docs.txt
├── CONTRIBUTING*.md
├── GOVERNANCE.md / CODE_OF_CONDUCT.md / SECURITY.md
├── ROADMAP.md / CHANGELOG.md / CITATION.cff
└── LICENSE / LICENSE-CODE / LICENSES.md
```

## Local work planned for later releases

`case-studies/`, `skills/`, and `social/` are retained in the maintainer's local workspace but intentionally excluded from the public v0.1. Cases will be published only with sanitized evidence; skills will be published only after they reflect actual practice and validation; social drafts will follow the supporting public content.

## Source-of-truth rule

Markdown files in the repository are the editable source of truth. Word and PDF editions may be generated for releases, presentations, or offline reading, but public corrections should be made in Markdown first.

## Content flow

```text
field experience
  → case evidence
  → method revision
  → regression test or quality gate
  → skill/template update
  → bilingual review
  → tagged release
  → focused LinkedIn post
```

## Adding a real project

1. Copy `templates/en/case-study.md` or `templates/zh-CN/case-study.md`.
2. Separate known facts, interpretation, metrics, and unknowns.
3. Add sanitized evidence rather than only a feature list.
4. Identify at least one human-owned decision and one AI-executed workflow.
5. Describe a failure, first divergence, correction, and lasting process or skill change.
6. Link the case to the relevant method chapter and, when available, a validated skill.
