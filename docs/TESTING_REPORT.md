# Testing Report

## Test types
| Type | Files | What is tested |
|------|-------|----------------|
| Unit | `tests/test_unit_database.py`, `test_unit_validation.py`, `test_unit_metrics.py` | Database functions, input validation, metric formulas, each in isolation |
| Integration | `tests/test_integration_routes.py` | Complete workflows through Flask routes + SQLite (add, view, update, delete, filter, errors, 404, health, metrics page) |

## Results (executed by the project author's tooling on Linux, Python 3.12.3)
| Item | Result |
|------|--------|
| Tests collected | 35 |
| Passed | 35 |
| Failed | 0 |
| Ruff lint (`ruff check .`) | All checks passed |
| Total coverage (line + branch) | **99%** (required minimum: 80%) |

| Module | Coverage |
|--------|----------|
| app/__init__.py | 94% |
| app/database.py | 100% |
| app/metrics.py | 100% |
| app/routes.py | 100% |
| app/validation.py | 100% |

## How to reproduce
```
coverage run -m pytest -v
coverage report
coverage html          # open htmlcov\index.html
ruff check .
```
**Team note:** re-run these on your own laptop and on GitHub Actions and paste your own
screenshots/output below. The table above is from the build environment, not your machine.

## Your own run (fill in)
- Date/time: ____  Tests passed: ____ / ____  Coverage: ____ %  Ruff: ____
- GitHub Actions run link: ____
