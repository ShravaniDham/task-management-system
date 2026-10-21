# Definition of Done (DoD)

A user story is **Done** only when ALL of these are true:

- [ ] Code is written and works in the browser (checked manually).
- [ ] Acceptance criteria for the story are met.
- [ ] Unit tests (and an integration test for the workflow) are written and pass.
- [ ] Test coverage stays at or above **80%** (`coverage report` fails below this).
- [ ] `ruff check .` and `ruff format --check .` report no problems.
- [ ] Code is pushed to GitHub and the **CI/CD pipeline is green** (Build, Test, Quality).
- [ ] Documentation is updated if behaviour changed.
- [ ] Reviewed by the other team member (pull request or pair review).
- [ ] Demonstrated to the Product Owner (sprint review).

**Where it is enforced automatically:** items 3-5 are checked by `.github/workflows/ci-cd.yml`.
