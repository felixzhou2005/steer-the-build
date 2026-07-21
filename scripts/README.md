# Repository validation scripts

Run from the repository root:

```bash
python scripts/check_links.py
python scripts/check_bilingual.py
python scripts/prepare_site.py
mkdocs build --strict
```

- `check_links.py` verifies relative Markdown links and local assets.
- `check_bilingual.py` verifies the expected English/Chinese pairs.
- `prepare_site.py` creates the ignored `.site-src/` staging directory used by MkDocs.

The scripts intentionally use only the Python standard library except the MkDocs build itself.
