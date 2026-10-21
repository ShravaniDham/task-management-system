"""Web routes: task list, add, edit, delete, health check and metrics dashboard."""

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

from . import database as db
from .metrics import get_sample_metrics
from .validation import validate_task

bp = Blueprint("tasks", __name__)


def _db_path():
    return current_app.config["DATABASE"]


def _form_values():
    return (
        request.form.get("title", ""),
        request.form.get("description", ""),
        request.form.get("status", "To Do"),
        request.form.get("priority", "Medium"),
    )


@bp.route("/")
def index():
    status = request.args.get("status", "").strip()
    search = request.args.get("q", "").strip()
    if status not in db.STATUSES:
        status = ""
    return render_template(
        "index.html",
        tasks=db.list_tasks(_db_path(), status or None, search or None),
        counts=db.count_by_status(_db_path()),
        statuses=db.STATUSES,
        priorities=db.PRIORITIES,
        selected_status=status,
        search=search,
    )


@bp.route("/tasks/add", methods=["POST"])
def add():
    title, description, status, priority = _form_values()
    errors = validate_task(title, status, priority)
    if errors:
        for message in errors:
            flash(message, "error")
    else:
        db.add_task(_db_path(), title, description, status, priority)
        flash("Task added successfully.", "success")
    return redirect(url_for("tasks.index"))


@bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def edit(task_id):
    task = db.get_task(_db_path(), task_id)
    if task is None:
        abort(404)
    if request.method == "POST":
        title, description, status, priority = _form_values()
        errors = validate_task(title, status, priority)
        if errors:
            for message in errors:
                flash(message, "error")
        else:
            db.update_task(_db_path(), task_id, title, description, status, priority)
            flash("Task updated successfully.", "success")
            return redirect(url_for("tasks.index"))
    return render_template(
        "edit.html", task=task, statuses=db.STATUSES, priorities=db.PRIORITIES
    )


@bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete(task_id):
    if not db.delete_task(_db_path(), task_id):
        abort(404)
    flash("Task deleted.", "success")
    return redirect(url_for("tasks.index"))


@bp.route("/health")
def health():
    """Used by Render (and by you) to check that the app is running."""
    return jsonify(status="ok")


@bp.route("/metrics")
def metrics():
    return render_template("metrics.html", data=get_sample_metrics())
