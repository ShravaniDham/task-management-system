# Task Management System (FA2 - Agile Software Development, Unit 3 and Unit 4)

A beginner-friendly Flask + SQLite web app with a GitHub Actions CI/CD pipeline:

**GitHub -> Build -> Automated Testing -> Code Quality Check -> Deployment**

## Features
- Add, View (with filter and search), Update and Delete tasks
- 35 automated tests (unit + integration), Coverage.py report, Ruff code quality check
- GitHub Actions pipeline with 4 ordered stages
- Render deployment configuration (optional, needs your own account)
- Agile documents and a metrics dashboard at `/metrics` (SAMPLE DATA, clearly labelled)

## Requirements
- Windows 10/11, **Python 3.11 or newer** (python.org, tick "Add Python to PATH")
- VS Code, Git, a GitHub account

## Quick start (Windows)
```
setup.bat        :: one time: creates .venv and installs dependencies
run_app.bat      :: starts the app at http://127.0.0.1:5000
run_checks.bat   :: tests + coverage + Ruff (same checks as the pipeline)
```
Manual commands (Command Prompt):
```
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
pytest -v
coverage run -m pytest
coverage report
coverage html            :: open htmlcov\index.html
ruff check .
ruff format --check .
```

## Project structure
```
app/
  __init__.py      app factory (create_app)
  database.py      SQLite functions: add/get/list/update/delete/count
  validation.py    form validation
  routes.py        web pages + /health
  metrics.py       Agile metric formulas + SAMPLE data
  templates/       base, index, edit, metrics HTML
  static/          css/style.css, js/main.js
tests/             unit tests + integration tests
docs/              8 Agile documents
.github/workflows/ci-cd.yml   the pipeline
render.yaml        Render deployment blueprint
pyproject.toml     Ruff + pytest configuration
.coveragerc        Coverage.py configuration
requirements.txt   dependencies (pinned)
run.py             entry point (python run.py / gunicorn run:app)
```

## CI/CD pipeline (`.github/workflows/ci-cd.yml`)
| Order | Job | Runs |
|-------|-----|------|
| 0 | GitHub trigger | on every push, pull request, or manual run |
| 1 | Build | install deps, compile, start-up check |
| 2 | Automated Testing | `coverage run -m pytest`, coverage must be >= 80% |
| 3 | Code Quality Check | `ruff check .` and `ruff format --check .` |
| 4 | Deployment | Render deploy hook; **only** on push to `main` **and** only if 1-3 passed |

Each job uses `needs:` so a failing stage blocks the next ones.

## Deployment setup (Render, optional - needs your own account)
Deployment is **not** active until you complete these steps. Until then the Deployment job
prints a warning and skips (it never pretends to deploy).

1. Push the project to GitHub (branch `main`).
2. On render.com: **New > Web Service** > connect your GitHub repo.
   Runtime Python, Build `pip install -r requirements.txt`, Start `gunicorn run:app`,
   Instance type **Free** (if available on your account), Health Check Path `/health`.
   Set **Auto-Deploy = Off** so only the pipeline deploys.
   (Alternative: New > Blueprint, which reads `render.yaml`.)
3. In the Render service: **Settings > Deploy Hook**, copy the URL (treat it like a password).
4. In GitHub: **Settings > Secrets and variables > Actions**
   - Secrets tab > New repository secret: name `RENDER_DEPLOY_HOOK_URL`, value = hook URL.
   - Variables tab (optional) > name `RENDER_APP_URL`, value = your `https://....onrender.com`
     (enables the post-deploy health check).
5. Push to `main`. After stages 1-3 pass, stage 4 triggers the deploy.

Limitations: free Render services sleep when idle (first request is slow) and their file
system is temporary, so SQLite tasks may reset on redeploy/restart. This is fine for a demo.

## Sample data notice
`/metrics` and `docs/AGILE_METRICS.md` use **sample data**. Replace with your real sprint data
before submitting if your faculty expects real measurements.

## Troubleshooting
| Problem | Fix |
|---------|-----|
| `'py' is not recognized` | Reinstall Python, tick "Add Python to PATH", reopen terminal |
| `running scripts is disabled` in PowerShell | Use Command Prompt, or run `.bat` files |
| Port 5000 in use | Close the other app or change the port in `run.py` |
| Pipeline red at Ruff | Run `ruff check . --fix` and `ruff format .`, commit, push |
| Deployment skipped | Secret `RENDER_DEPLOY_HOOK_URL` not set (see above) |
