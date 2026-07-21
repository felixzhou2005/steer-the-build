# Quick start

## Use this package to create the GitHub repository

1. Create a **public, empty** repository named `steer-the-build`.
2. Do not initialize it with a README, `.gitignore`, or license.
3. Extract the package and enter the `steer-the-build` directory.
4. Verify the configured repository URL, then fill in the public author and maintainer details.
5. Validate and push:

```bash
python scripts/check_links.py
python scripts/check_bilingual.py
python -m pip install -r requirements-docs.txt
python scripts/prepare_site.py
mkdocs build --strict

git init
git add .
git commit -m "docs: launch Steer the Build v0.1.0"
git branch -M main
git remote add origin git@github.com:<YOUR_GITHUB_USERNAME>/steer-the-build.git
git push -u origin main
```

6. Follow [the post-creation checklist](meta/post-create-checklist.md).

## Use the method in another software project

Copy these files first:

- `templates/en/project-ai-constitution.md`
- `templates/en/product-requirements.md`
- `templates/en/architecture-design.md`
- `templates/en/implementation-plan.md`
- `templates/en/test-strategy.md`
- `templates/en/observability-spec.md`
- `templates/en/skill-spec.md` when a repeated lesson is ready to become a validated skill
