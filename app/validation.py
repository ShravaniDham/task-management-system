"""Input validation for task forms."""

from .database import PRIORITIES, STATUSES

MAX_TITLE_LENGTH = 100


def validate_task(title, status, priority):
    """Return a list of error messages (an empty list means the input is valid)."""
    errors = []
    title = (title or "").strip()
    if not title:
        errors.append("Title is required.")
    elif len(title) > MAX_TITLE_LENGTH:
        errors.append(f"Title must be at most {MAX_TITLE_LENGTH} characters.")
    if status not in STATUSES:
        errors.append("Status must be To Do, In Progress or Done.")
    if priority not in PRIORITIES:
        errors.append("Priority must be Low, Medium or High.")
    return errors
