#!/usr/bin/env python3
"""Validate relative links in Markdown files.

External URLs, mail links, pure anchors, and explicit placeholders are ignored.
The script does not attempt to validate remote availability.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {'.git', '.site-src', 'site', '.venv', '__pycache__'}
LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
HTML_LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
FENCE_RE = re.compile(r'^\s*(```|~~~)')


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob('*.md')
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def strip_code_fences(text: str) -> str:
    kept: list[str] = []
    in_fence = False
    fence = ''
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence = True
                fence = marker[0]
            elif marker[0] == fence:
                in_fence = False
            continue
        if not in_fence:
            kept.append(line)
    return '\n'.join(kept)


def normalize(raw: str) -> str:
    value = raw.strip()
    if value.startswith('<') and value.endswith('>'):
        value = value[1:-1]
    # Markdown permits an optional title after a whitespace separator.
    if ' "' in value:
        value = value.split(' "', 1)[0]
    if " '" in value:
        value = value.split(" '", 1)[0]
    return unquote(value)


def is_ignored(link: str) -> bool:
    lowered = link.lower()
    return (
        not link
        or link.startswith('#')
        or lowered.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:'))
        or '<repository_url>' in lowered
        or 'replace_with_username' in lowered
        or link.startswith('{')
    )


def target_path(source: Path, link: str) -> Path:
    path_part = link.split('#', 1)[0].split('?', 1)[0]
    if path_part.startswith('/'):
        return ROOT / path_part.lstrip('/')
    return (source.parent / path_part).resolve()


def main() -> int:
    failures: list[tuple[Path, str, Path]] = []
    checked = 0
    for source in markdown_files():
        text = strip_code_fences(source.read_text(encoding='utf-8'))
        links = LINK_RE.findall(text) + HTML_LINK_RE.findall(text)
        for raw in links:
            link = normalize(raw)
            if is_ignored(link):
                continue
            target = target_path(source, link)
            checked += 1
            try:
                target.relative_to(ROOT)
            except ValueError:
                failures.append((source, link, target))
                continue
            if not target.exists():
                failures.append((source, link, target))

    if failures:
        print(f'Broken local links: {len(failures)}', file=sys.stderr)
        for source, link, target in failures:
            print(
                f'- {source.relative_to(ROOT)} -> {link} '
                f'(resolved: {target})',
                file=sys.stderr,
            )
        return 1

    print(f'Link check passed: {checked} local links across {len(markdown_files())} Markdown files.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
