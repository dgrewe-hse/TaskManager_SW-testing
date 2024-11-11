# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager

# TODO: GRUPPE 1 - Add BDD steps for removing a task

@given('the user is within the task manager application')
def step_given_user_is_using_task_manager_application(context):
    """Set up the task manager application for the user."""
    context.task_manager = TaskManager()

@given('the name of the irrelevant task is available')
def step_user_defines_task_as_irrelevant(context):
    """Set up the task management application for the user."""
    context.task_name = "Task to be erased"

@when('the user erases the task with the name "{task_name}"')
def step_when_user_erases_task (context, task_name):
    """Erase the task with the given name"""
    context.taskmanager.erase_task(task_name)  #Erase task using task manager


@then('the task disappears from the task list')
def step_when_the_task_disappears_from_the_list(context):
    """Check that the erased task is not in the list of tasks anymore"""
    tasks = context.task_manager.get_all_tasks() #Retrieve all tasks
    assert any(task['description'] == context.task_manager.tasks[-1]['description'] for task in tasks), \
        "Task was succesfully erased"
