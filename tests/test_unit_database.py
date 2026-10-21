"""UNIT TESTS - database functions in isolation."""

import sqlite3

from app import database as db


def test_init_db_creates_tasks_table(db_path):
    conn = sqlite3.connect(db_path)
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    conn.close()
    assert ("tasks",) in tables


def test_add_and_get_task(db_path):
    task_id = db.add_task(db_path, "  Write report  ", "Unit 3", "In Progress", "High")
    task = db.get_task(db_path, task_id)
    assert task["title"] == "Write report"  # whitespace trimmed
    assert task["status"] == "In Progress"
    assert task["priority"] == "High"


def test_get_task_returns_none_for_unknown_id(db_path):
    assert db.get_task(db_path, 999) is None


def test_list_tasks_newest_first(db_path):
    db.add_task(db_path, "First")
    db.add_task(db_path, "Second")
    titles = [t["title"] for t in db.list_tasks(db_path)]
    assert titles == ["Second", "First"]


def test_list_tasks_filter_by_status(db_path):
    db.add_task(db_path, "A", status="Done")
    db.add_task(db_path, "B", status="To Do")
    result = db.list_tasks(db_path, status="Done")
    assert [t["title"] for t in result] == ["A"]


def test_list_tasks_search_by_title(db_path):
    db.add_task(db_path, "Buy milk")
    db.add_task(db_path, "Study agile")
    result = db.list_tasks(db_path, search="agile")
    assert [t["title"] for t in result] == ["Study agile"]


def test_update_task_changes_values(db_path):
    task_id = db.add_task(db_path, "Old")
    assert db.update_task(db_path, task_id, "New", "desc", "Done", "Low") is True
    task = db.get_task(db_path, task_id)
    assert (task["title"], task["status"], task["priority"]) == ("New", "Done", "Low")


def test_update_task_unknown_id_returns_false(db_path):
    assert db.update_task(db_path, 42, "x", "", "To Do", "Low") is False


def test_delete_task(db_path):
    task_id = db.add_task(db_path, "Temp")
    assert db.delete_task(db_path, task_id) is True
    assert db.get_task(db_path, task_id) is None


def test_delete_task_unknown_id_returns_false(db_path):
    assert db.delete_task(db_path, 42) is False


def test_count_by_status(db_path):
    db.add_task(db_path, "A", status="Done")
    db.add_task(db_path, "B", status="Done")
    db.add_task(db_path, "C", status="To Do")
    assert db.count_by_status(db_path) == {"To Do": 1, "In Progress": 0, "Done": 2}
