# Release checklist

## Content integrity

- [ ] All changed claims have an identified evidence level.
- [ ] Project metrics are measured, sourced, or marked as estimates.
- [ ] No private customer, user, credential, endpoint, or dataset detail is exposed.
- [ ] English and Chinese status is recorded.
- [ ] Related work and tool-version-sensitive claims have been rechecked.
- [ ] Case studies distinguish facts, interpretation, and unknowns.

## Repository quality

- [ ] `python scripts/check_links.py` passes.
- [ ] `python scripts/check_bilingual.py` passes.
- [ ] `python scripts/prepare_site.py && mkdocs build --strict` passes.
- [ ] GitHub Actions pass on the release commit.
- [ ] Placeholder scan has been reviewed, not blindly cleared.
- [ ] `CHANGELOG.md`, `CITATION.cff`, and version labels are updated.

## Governance

- [ ] Security-sensitive contributions were reviewed privately where necessary.
- [ ] Contributor attribution is correct.
- [ ] License boundaries between prose and reusable assets remain clear.
- [ ] Breaking changes to template or skill contracts are described.

## Publication

- [ ] Create signed or annotated tag `vX.Y.Z`.
- [ ] Generate release notes from the changelog.
- [ ] Verify the GitHub Pages site after deployment.
- [ ] Update deep links in scheduled LinkedIn material if paths changed.
- [ ] Open a release discussion for feedback and counterexamples.
