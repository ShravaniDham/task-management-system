# How CI/CD Supports Agile Delivery

## The pipeline
`GitHub -> Build -> Automated Testing -> Code Quality Check -> Deployment`
defined in `.github/workflows/ci-cd.yml` (GitHub Actions). Each stage is a job that
`needs` the previous one, so a failure stops everything after it.

| Stage | What it does | Agile benefit |
|-------|--------------|---------------|
| GitHub | A push or pull request triggers the workflow | Small, frequent changes are integrated continuously |
| Build | Installs dependencies, compiles code, starts the app | Broken code is found within minutes |
| Automated Testing | Runs 35 unit + integration tests with Coverage.py | Fast feedback and safe changes; supports the DoD |
| Code Quality Check | Ruff lint and format check | Consistent, clean code; less technical debt |
| Deployment | Triggers a Render deploy hook, only on `main` and only if all earlier stages pass | A working increment is always available for sprint review |

## Why it helps Agile
- **Continuous integration** gives quick feedback, so defects are cheaper to fix (lower defect density).
- **Automated tests** replace slow manual checking, so the team can finish stories faster (shorter cycle time).
- **Quality gates** (coverage >= 80%, Ruff) enforce the Definition of Done automatically.
- **Automated deployment** makes releases small and repeatable, so a "potentially shippable increment" exists every sprint.
- **Visible results** (green/red pipeline, coverage report, metrics page) support transparency and inspection.

## Deployment note
Deployment needs a Render account and the secret `RENDER_DEPLOY_HOOK_URL`. Without that
secret, the deploy job prints a warning and **skips** deployment; it does not claim a deployment
happened. See README for setup.
