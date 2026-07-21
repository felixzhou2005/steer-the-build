#!/usr/bin/env python3
"""Check the expected bilingual file pairs."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    missing: list[str] = []
    pairs = 0

    # Core chapters.
    for en in sorted((ROOT / 'docs/en').glob('*.md')):
        zh = ROOT / 'docs/zh-CN' / en.name
        if en.name == 'index.md':
            zh = ROOT / 'docs/zh-CN/index.md'
        pairs += 1
        if not zh.exists():
            missing.append(f'{rel(en)} -> {rel(zh)}')

    # Templates.
    for en in sorted((ROOT / 'templates/en').glob('*.md')):
        zh = ROOT / 'templates/zh-CN' / en.name
        pairs += 1
        if not zh.exists():
            missing.append(f'{rel(en)} -> {rel(zh)}')

    # Optional cases. Local drafts are intentionally absent from public v0.1.
    cases_root = ROOT / 'case-studies'
    if cases_root.exists():
        for case_dir in sorted(p for p in cases_root.iterdir() if p.is_dir()):
            en = case_dir / 'README.md'
            zh = case_dir / 'README.zh-CN.md'
            pairs += 1
            if not en.exists() or not zh.exists():
                missing.append(f'{rel(case_dir)} requires README.md and README.zh-CN.md')

    # Optional skills. Validated real-world skills will enter a later release.
    for layer in ('base', 'domain'):
        parent = ROOT / 'skills' / layer
        if not parent.exists():
            continue
        for skill_dir in sorted(p for p in parent.iterdir() if p.is_dir()):
            en = skill_dir / 'SKILL.md'
            zh = skill_dir / 'SKILL.zh-CN.md'
            pairs += 1
            if not en.exists() or not zh.exists():
                missing.append(f'{rel(skill_dir)} requires SKILL.md and SKILL.zh-CN.md')

    # Root/index and research/meta pairs.
    explicit = [
        ('README.md', 'README.zh-CN.md'),
        ('QUICKSTART.md', 'QUICKSTART.zh-CN.md'),
        ('PROJECT_STRUCTURE.md', 'PROJECT_STRUCTURE.zh-CN.md'),
        ('CONTRIBUTING.md', 'CONTRIBUTING.zh-CN.md'),
        ('templates/README.md', 'templates/README.zh-CN.md'),
        ('research/README.md', 'research/README.zh-CN.md'),
        ('research/related-work.md', 'research/related-work.zh-CN.md'),
        ('research/differentiation.md', 'research/differentiation.zh-CN.md'),
        ('research/glossary.md', 'research/glossary.zh-CN.md'),
        ('research/source-review-policy.md', 'research/source-review-policy.zh-CN.md'),
        ('meta/README.md', 'meta/README.zh-CN.md'),
        ('meta/editorial-guide.md', 'meta/editorial-guide.zh-CN.md'),
        ('meta/translation-guide.md', 'meta/translation-guide.zh-CN.md'),
        ('meta/content-status.md', 'meta/content-status.zh-CN.md'),
        ('meta/release-checklist.md', 'meta/release-checklist.zh-CN.md'),
        ('meta/post-create-checklist.md', 'meta/post-create-checklist.zh-CN.md'),
        ('meta/maintainer-backlog.md', 'meta/maintainer-backlog.zh-CN.md'),
    ]
    for a, b in explicit:
        pairs += 1
        if not (ROOT / a).exists() or not (ROOT / b).exists():
            missing.append(f'{a} <-> {b}')

    optional_explicit = [
        ('case-studies/README.md', 'case-studies/README.zh-CN.md'),
        ('skills/README.md', 'skills/README.zh-CN.md'),
    ]
    for a, b in optional_explicit:
        path_a = ROOT / a
        path_b = ROOT / b
        if not path_a.exists() and not path_b.exists():
            continue
        pairs += 1
        if not path_a.exists() or not path_b.exists():
            missing.append(f'{a} <-> {b}')

    if missing:
        print(f'Bilingual check failed: {len(missing)} missing pair(s).', file=sys.stderr)
        for item in missing:
            print(f'- {item}', file=sys.stderr)
        return 1

    print(f'Bilingual check passed: {pairs} expected pairs are present.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
