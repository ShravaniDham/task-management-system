"""UNIT TESTS - input validation."""

from app.validation import validate_task


def test_valid_input_has_no_errors():
    assert validate_task("Learn CI/CD", "To Do", "High") == []


def test_empty_title_is_rejected():
    assert "Title is required." in validate_task("   ", "To Do", "Low")


def test_none_title_is_rejected():
    assert validate_task(None, "To Do", "Low") != []


def test_too_long_title_is_rejected():
    errors = validate_task("x" * 101, "To Do", "Low")
    assert any("at most 100" in e for e in errors)


def test_invalid_status_is_rejected():
    assert any("Status" in e for e in validate_task("Ok", "Blocked", "Low"))


def test_invalid_priority_is_rejected():
    assert any("Priority" in e for e in validate_task("Ok", "To Do", "Urgent"))
