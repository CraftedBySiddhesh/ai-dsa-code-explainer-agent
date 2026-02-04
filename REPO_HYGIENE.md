# Repo Hygiene & Merge Quality Gates

## Recommended branch protection (GitHub settings)
Enable on `main`:
- Require PR before merge
- Require at least 1 approval
- Require status checks: **CI**
- Require conversation resolution
- (Optional) Require signed commits

## Local gates (developer machine)
- Install hooks: `pre-commit install`
- Run before pushing: `pre-commit run -a`

## CI gates (automatic)
- Ruff lint
- Ruff format check
- Black format check
- Mypy (non-blocking; make blocking by removing `|| true`)
