# Agile Metrics

> **SAMPLE DATA.** The numbers below are illustrative values used to demonstrate the
> metrics and the dashboard (`/metrics` page). They are **not** measured from a real team.
> Replace them with your real sprint data in `app/metrics.py` (and then in this file).

## Definitions
| Metric | Meaning | Formula |
|--------|---------|---------|
| Sprint velocity | Story points completed in a sprint | sum of points of Done stories |
| Defect density | Defects per 1000 lines of code | defects / KLOC |
| Lead time | Time from story creation to Done | done date - created date |
| Cycle time | Time from work started to Done | done date - started date |

## Sprint data (sample)
| Sprint | Planned | Completed (velocity) | Defects | KLOC | Defects/KLOC |
|--------|---------|----------------------|---------|------|--------------|
| Sprint 1 | 20 | 18 | 3 | 0.5 | 6.00 |
| Sprint 2 | 22 | 21 | 2 | 0.6 | 3.33 |
| Sprint 3 | 24 | 24 | 1 | 0.4 | 2.50 |
| **Average / overall** | | **21.0** | 6 | 1.5 | **4.00** |

## Story data (sample)
| Story | Created | Started | Done | Lead time (days) | Cycle time (days) |
|-------|---------|---------|------|------------------|-------------------|
| US-1 | 2026-09-23 | 2026-09-24 | 2026-09-28 | 5 | 4 |
| US-2 | 2026-09-23 | 2026-09-25 | 2026-09-29 | 6 | 4 |
| US-3 | 2026-09-23 | 2026-09-30 | 2026-10-03 | 10 | 3 |
| US-4 | 2026-09-23 | 2026-10-01 | 2026-10-04 | 11 | 3 |
| US-5 | 2026-09-25 | 2026-10-02 | 2026-10-08 | 13 | 6 |
| **Average** | | | | **9.0** | **4.0** |

## Interpretation (sample)
- Velocity rises 18 -> 21 -> 24: the team is delivering more per sprint.
- Defect density falls 6.0 -> 2.5: automated tests and Ruff catch problems earlier.
- Lead time (9 days) is longer than cycle time (4 days): stories waited in the backlog before work began.

Dashboard: run the app and open http://127.0.0.1:5000/metrics.
