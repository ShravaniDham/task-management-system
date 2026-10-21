"""INTEGRATION TESTS - full workflows through the Flask routes and SQLite."""

from app import database as db


def _add(client, title="Demo task", **extra):
    data = {"title": title, "description": "d", "status": "To Do", "priority": "Medium"}
    data.update(extra)
    return client.post("/tasks/add", data=data, follow_redirects=True)


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Task Management System" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_task_then_view_it(client):
    response = _add(client, "Prepare FA2")
    assert b"Task added successfully." in response.data
    assert b"Prepare FA2" in response.data


def test_add_task_with_empty_title_shows_error(client):
    response = _add(client, "   ")
    assert b"Title is required." in response.data


def test_add_task_with_invalid_status_shows_error(client):
    response = _add(client, "Bad", status="Blocked")
    assert b"Status must be" in response.data


def test_full_crud_workflow(client):
    # Create
    _add(client, "Original title")
    task_id = db.list_tasks(client.application.config["DATABASE"])[0]["id"]

    # Read (edit page shows current values)
    page = client.get(f"/tasks/{task_id}/edit")
    assert page.status_code == 200
    assert b"Original title" in page.data

    # Update
    response = client.post(
        f"/tasks/{task_id}/edit",
        data={"title": "Updated title", "description": "x",
              "status": "Done", "priority": "High"},
        follow_redirects=True,
    )  # fmt: skip
    assert b"Task updated successfully." in response.data
    assert b"Updated title" in response.data
    assert b"Original title" not in response.data

    # Delete
    response = client.post(f"/tasks/{task_id}/delete", follow_redirects=True)
    assert b"Task deleted." in response.data
    assert b"Updated title" not in response.data


def test_update_with_invalid_data_keeps_old_values(client):
    _add(client, "Keep me")
    path = client.application.config["DATABASE"]
    task_id = db.list_tasks(path)[0]["id"]
    response = client.post(
        f"/tasks/{task_id}/edit",
        data={"title": "", "description": "", "status": "To Do", "priority": "Low"},
    )
    assert b"Title is required." in response.data
    assert db.get_task(path, task_id)["title"] == "Keep me"


def test_edit_unknown_task_returns_404(client):
    assert client.get("/tasks/999/edit").status_code == 404


def test_delete_unknown_task_returns_404(client):
    assert client.post("/tasks/999/delete").status_code == 404


def test_filter_by_status_and_search(client):
    _add(client, "Finished work", status="Done")
    _add(client, "Pending work", status="To Do")
    done_only = client.get("/?status=Done")
    assert b"Finished work" in done_only.data
    assert b"Pending work" not in done_only.data
    searched = client.get("/?q=Pending")
    assert b"Pending work" in searched.data
    assert b"Finished work" not in searched.data


def test_unknown_status_filter_is_ignored(client):
    _add(client, "Visible task")
    assert b"Visible task" in client.get("/?status=Nonsense").data


def test_metrics_page_is_labelled_as_sample_data(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"SAMPLE DATA" in response.data
    assert b"Sprint 1" in response.data
