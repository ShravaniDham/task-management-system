"""SQLite data-access functions for tasks (Create, Read, Update, Delete)."""

import sqlite3
from contextlib import closing
from datetime import UTC, datetime

STATUSES = ("To Do", "In Progress", "Done")
PRIORITIES = ("Low", "Medium", "High")

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    status      TEXT NOT NULL DEFAULT 'To Do',
    priority    TEXT NOT NULL DEFAULT 'Medium',
    created_at  TEXT NOT NULL
);
"""


def get_connection(db_path):
    """Open a SQLite connection that returns rows like dictionaries."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path):
    """Create the tasks table if it does not exist yet."""
    with closing(get_connection(db_path)) as conn:
        conn.executescript(SCHEMA)
        conn.commit()


def add_task(db_path, title, description="", status="To Do", priority="Medium"):
    """CREATE: insert a task and return its new id."""
    created_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M")
    with closing(get_connection(db_path)) as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, status, priority, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (title.strip(), description.strip(), status, priority, created_at),
        )
        conn.commit()
        return cursor.lastrowid


def get_task(db_path, task_id):
    """READ one task as a dict, or None if it does not exist."""
    with closing(get_connection(db_path)) as conn:
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    return dict(row) if row else None


def list_tasks(db_path, status=None, search=None):
    """READ many tasks, newest first, optionally filtered by status / title text."""
    query = "SELECT * FROM tasks WHERE 1 = 1"
    params = []
    if status:
        query += " AND status = ?"
        params.append(status)
    if search:
        query += " AND title LIKE ?"
        params.append(f"%{search}%")
    query += " ORDER BY id DESC"
    with closing(get_connection(db_path)) as conn:
        rows = conn.execute(query, params).fetchall()
    return [dict(row) for row in rows]


def update_task(db_path, task_id, title, description, status, priority):
    """UPDATE a task. Returns True if a row was changed, False if id not found."""
    with closing(get_connection(db_path)) as conn:
        cursor = conn.execute(
            "UPDATE tasks SET title = ?, description = ?, status = ?, priority = ? "
            "WHERE id = ?",
            (title.strip(), description.strip(), status, priority, task_id),
        )
        conn.commit()
        return cursor.rowcount > 0


def delete_task(db_path, task_id):
    """DELETE a task. Returns True if a row was removed, False if id not found."""
    with closing(get_connection(db_path)) as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0


def count_by_status(db_path):
    """Return {'To Do': n, 'In Progress': n, 'Done': n} for the summary cards."""
    counts = dict.fromkeys(STATUSES, 0)
    with closing(get_connection(db_path)) as conn:
        rows = conn.execute(
            "SELECT status, COUNT(*) AS total FROM tasks GROUP BY status"
        ).fetchall()
    for row in rows:
        counts[row["status"]] = row["total"]
    return counts
