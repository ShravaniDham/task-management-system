"""Agile metric calculations + SAMPLE data for the dashboard.

IMPORTANT: the numbers returned by get_sample_metrics() are SAMPLE DATA for
demonstration. Replace them with your own team's real sprint data.
"""

from datetime import date


def calc_velocity(sprints):
    """Velocity = story points COMPLETED in each sprint."""
    return [sprint["completed"] for sprint in sprints]


def average(values):
    """Average rounded to 2 decimals (0 for an empty list)."""
    return round(sum(values) / len(values), 2) if values else 0


def calc_defect_density(defects, kloc):
    """Defect density = defects found per 1000 lines of code (KLOC)."""
    if kloc <= 0:
        return 0
    return round(defects / kloc, 2)


def lead_time_days(created, done):
    """Lead time = days from request/creation until the work is Done."""
    return (date.fromisoformat(done) - date.fromisoformat(created)).days


def cycle_time_days(started, done):
    """Cycle time = days from work started until the work is Done."""
    return (date.fromisoformat(done) - date.fromisoformat(started)).days


SAMPLE_SPRINTS = [
    {"name": "Sprint 1", "planned": 20, "completed": 18, "defects": 3, "kloc": 0.5},
    {"name": "Sprint 2", "planned": 22, "completed": 21, "defects": 2, "kloc": 0.6},
    {"name": "Sprint 3", "planned": 24, "completed": 24, "defects": 1, "kloc": 0.4},
]

SAMPLE_STORIES = [
    {"id": "US-1", "title": "Add a task", "created": "2026-09-23",
     "started": "2026-09-24", "done": "2026-09-28"},
    {"id": "US-2", "title": "View tasks", "created": "2026-09-23",
     "started": "2026-09-25", "done": "2026-09-29"},
    {"id": "US-3", "title": "Update a task", "created": "2026-09-23",
     "started": "2026-09-30", "done": "2026-10-03"},
    {"id": "US-4", "title": "Delete a task", "created": "2026-09-23",
     "started": "2026-10-01", "done": "2026-10-04"},
    {"id": "US-5", "title": "CI/CD pipeline and metrics", "created": "2026-09-25",
     "started": "2026-10-02", "done": "2026-10-08"},
]  # fmt: skip


def get_sample_metrics():
    """Build every number shown on the /metrics dashboard from the sample data."""
    sprints = []
    for sprint in SAMPLE_SPRINTS:
        row = dict(sprint)
        row["defect_density"] = calc_defect_density(sprint["defects"], sprint["kloc"])
        sprints.append(row)

    stories = []
    for story in SAMPLE_STORIES:
        row = dict(story)
        row["lead_time"] = lead_time_days(story["created"], story["done"])
        row["cycle_time"] = cycle_time_days(story["started"], story["done"])
        stories.append(row)

    total_defects = sum(s["defects"] for s in SAMPLE_SPRINTS)
    total_kloc = sum(s["kloc"] for s in SAMPLE_SPRINTS)
    return {
        "sprints": sprints,
        "stories": stories,
        "average_velocity": average(calc_velocity(SAMPLE_SPRINTS)),
        "overall_defect_density": calc_defect_density(total_defects, total_kloc),
        "average_lead_time": average([s["lead_time"] for s in stories]),
        "average_cycle_time": average([s["cycle_time"] for s in stories]),
    }
