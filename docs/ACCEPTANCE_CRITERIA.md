# Acceptance Criteria

Format: **Given** (starting situation) **When** (action) **Then** (expected result).
Each criterion is covered by an automated test (test name in brackets).

## US-1 Add a task
1. **Given** I am on the home page, **when** I enter a title and click *Add Task*,
   **then** I see "Task added successfully." and the task in the list.
   (`test_add_task_then_view_it`)
2. **Given** the title is empty or only spaces, **when** I submit, **then** I see
   "Title is required." and no task is created. (`test_add_task_with_empty_title_shows_error`)
3. **Given** a title longer than 100 characters, **then** it is rejected.
   (`test_too_long_title_is_rejected`)

## US-2 View / filter tasks
1. **Given** tasks exist, **when** I open the home page, **then** I see them newest first.
   (`test_list_tasks_newest_first`)
2. **Given** tasks with different statuses, **when** I filter by "Done", **then** only Done
   tasks are shown. (`test_filter_by_status_and_search`)
3. **Given** I type text in the search box, **then** only tasks whose title contains it appear.
   (`test_list_tasks_search_by_title`)

## US-3 Update a task
1. **Given** a task exists, **when** I click *Edit*, change values and save, **then** I see
   "Task updated successfully." and the new values. (`test_full_crud_workflow`)
2. **Given** I clear the title and save, **then** an error is shown and the old values are kept.
   (`test_update_with_invalid_data_keeps_old_values`)
3. **Given** the task id does not exist, **then** the app returns 404.
   (`test_edit_unknown_task_returns_404`)

## US-4 Delete a task
1. **Given** a task exists, **when** I click *Delete* and confirm, **then** I see "Task deleted."
   and it disappears. (`test_full_crud_workflow`)
2. **Given** the task id does not exist, **then** the app returns 404.
   (`test_delete_unknown_task_returns_404`)

## US-5 Pipeline and metrics
1. **Given** I push code to GitHub, **then** the workflow runs Build, Automated Testing,
   Code Quality Check and Deployment in that order. (GitHub Actions tab)
2. **Given** any earlier stage fails, **then** the Deployment stage does not run.
3. **Given** I open `/metrics`, **then** I see velocity, defect density, lead time and cycle
   time, clearly labelled as SAMPLE DATA. (`test_metrics_page_is_labelled_as_sample_data`)
