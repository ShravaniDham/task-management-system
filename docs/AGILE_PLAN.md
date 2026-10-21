# Agile Project Plan - Task Management System

**Course:** Agile Software Development (FA2, Unit 3 and Unit 4)
**Team:** _(write your 2 names and roll numbers here)_
**Methodology:** Scrum (3 one-week sprints)

## Product Goal
A simple web app where a user can add, view, update and delete tasks, delivered through an
automated CI/CD pipeline.

## Product Backlog (priority order)
| ID | User story | Points | Sprint |
|----|-----------|--------|--------|
| US-1 | Add a task | 5 | 1 |
| US-2 | View / filter tasks | 3 | 1 |
| US-3 | Update a task | 5 | 2 |
| US-4 | Delete a task | 3 | 2 |
| US-5 | CI/CD pipeline and metrics dashboard | 8 | 3 |

Full stories: `USER_STORIES.md`.

## Sprint Planning
| Sprint | Dates (planned) | Sprint goal | Stories |
|--------|-----------------|-------------|---------|
| 1 | 23 Sep - 29 Sep 2026 | Users can create and see tasks | US-1, US-2 |
| 2 | 30 Sep - 06 Oct 2026 | Users can change and remove tasks | US-3, US-4 |
| 3 | 07 Oct - 13 Oct 2026 | Automated pipeline, deployment, metrics, documentation | US-5 |

## Ceremonies (kept simple)
- **Sprint planning:** pick stories for the sprint and agree acceptance criteria.
- **Daily stand-up (5 min):** what I did, what I will do, any blocker.
- **Sprint review:** demo the working app to the faculty/team.
- **Retrospective:** one thing to keep, one thing to improve.

## Roles
- **Product Owner / Scrum Master / Developers:** shared between the two team members
  (write who played which role).

## Quality practices
Definition of Done: `DEFINITION_OF_DONE.md`. Every push runs the CI/CD pipeline
(build, tests, Ruff, deploy).
