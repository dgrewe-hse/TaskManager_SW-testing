# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then    

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager

@given('the user is using the task manager application for updating a task')
def step_given_user_on_application(context):
    """Set up the task management application for the user."""
    context.task_manager = TaskManager()  # Initialize the task manager
    context.task_manager.clear_tasks()  # Clear any existing tasks for a fresh start

@given('a task is existing in the total list of tasks with the name "{task_name}" and the description "{task_description}"')
def step_given_task_existing_in_list(context, task_name, task_description):
    """Set up the task management application for the user."""
    context.task_name = "Complete project report"
    context.task_description = "Complete the project report"
    context.task_manager.add_task(task_name, task_description)  # Add the task using the task manager

@when('the user updates the existing task with the name "{new_task_name}" and the description "{new_task_description}"')
def step_when_user_updates_task(context, new_task_name, new_task_description):
    """Update existing task with the given new task name and new description."""
    context.task_manager.update_task(new_task_name, new_task_description)  # Add the task using the task manager

@then('the changed task should appear updated in the total list of tasks')
def step_then_updated_task_appears_in_list(context):
    """Check that the updated task is in the list of tasks."""
    tasks = context.task_manager.get_all_tasks()  # Retrieve all tasks
    assert any(task['description'] == context.task_manager.tasks[-1]['description'] for task in tasks), \
        "The task was not found in the list of tasks." 