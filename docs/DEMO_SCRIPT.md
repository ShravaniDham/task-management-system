# Demo Script (1-2 minutes, record in YOUR OWN voice)

The notice requires original voice narration; AI-generated voice is not allowed. Read this in
your own words, do not copy it word-for-word.

| Time | Show on screen | Say (in your own words) |
|------|----------------|-------------------------|
| 0:00-0:10 | Title slide or GitHub repo | "We are [names]. Our project is a Task Management System built with Flask and SQLite, using Agile and CI/CD." |
| 0:10-0:25 | docs folder: user stories, DoD, acceptance criteria | "We planned 5 user stories in 3 sprints, with a Definition of Done and acceptance criteria." |
| 0:25-0:45 | App in browser: add, edit, delete a task | "The app supports add, view, update and delete." |
| 0:45-1:25 | GitHub Actions run: 4 green stages, click each | "On every push, GitHub Actions runs Build, Automated Testing, Code Quality with Ruff, then Deployment. Deployment only runs if earlier stages pass." |
| 1:25-1:40 | Coverage report + /metrics page | "35 tests pass with 99% coverage. The dashboard shows velocity, defect density, lead and cycle time (sample data)." |
| 1:40-1:55 | Live Render URL (only if deployed) | "The app is deployed on Render." (skip if not deployed; say honestly what you did) |

## Evidence checklist (screenshots)
- [ ] App home page with task list; add/edit/delete messages
- [ ] Terminal: `pytest` all passing
- [ ] Coverage HTML report (`htmlcov/index.html`)
- [ ] Terminal: `ruff check .` -> All checks passed
- [ ] GitHub repo with files
- [ ] GitHub Actions run showing the 4 stages in order
- [ ] A failed run (optional) showing Deployment skipped
- [ ] Render dashboard + live URL `/health` (only if actually deployed)
- [ ] docs folder files and /metrics page
