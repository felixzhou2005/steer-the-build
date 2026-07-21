#!/usr/bin/env python3
"""Stage public repository Markdown into .site-src for MkDocs.

The public v0.1 keeps templates, research, and governance at the top level.
Cases and validated real-world skills are optional later-release sections.
MkDocs expects one docs root, so this script creates an ignored mirror.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / '.site-src'
DIRECTORIES = ('docs', 'research', 'meta')
OPTIONAL_DIRECTORIES = ('case-studies', 'skills')
ROOT_FILES = (
    'README.md',
    'README.zh-CN.md',
    'QUICKSTART.md',
    'QUICKSTART.zh-CN.md',
    'PROJECT_STRUCTURE.md',
    'PROJECT_STRUCTURE.zh-CN.md',
    'CONTRIBUTING.md',
    'CONTRIBUTING.zh-CN.md',
    'ROADMAP.md',
    'SECURITY.md',
    'LICENSES.md',
    'CODE_OF_CONDUCT.md',
    'GOVERNANCE.md',
)


def main() -> int:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    for directory in DIRECTORIES:
        source = ROOT / directory
        shutil.copytree(source, DEST / directory)

    for directory in OPTIONAL_DIRECTORIES:
        source = ROOT / directory
        if source.exists():
            shutil.copytree(source, DEST / directory)

    # MkDocs reserves a top-level 'templates/' directory for theme files.
    # Stage the public template library under a different URL and rewrite only
    # Markdown link destinations; repository path examples remain unchanged.
    shutil.copytree(ROOT / 'templates', DEST / 'template-library')

    for filename in ROOT_FILES:
        shutil.copy2(ROOT / filename, DEST / filename)

    link_pattern = re.compile(r'(\]\((?:\.\./)*)templates/')
    for markdown in DEST.rglob('*.md'):
        content = markdown.read_text(encoding='utf-8')
        content = link_pattern.sub(r'\1template-library/', content)
        markdown.write_text(content, encoding='utf-8')

    print(f'Prepared MkDocs source at {DEST} ({sum(1 for _ in DEST.rglob("*.md"))} Markdown files).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
