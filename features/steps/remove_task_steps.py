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
    context.task_manager = TaskManager() # Initialize the task manager
    context.task_manager.clear_tasks() # clear all tasks for fresh start

@given('a task with the name "{task_name}" is in the task list')
def step_user_adds_task_to_list(context, task_name):
    """Set up the task management application for the user. Add a task."""
    context.task_manager.add_task(task_name)
    context.task_name = task_name

@when('the user erases the task with the name "{task_name}"')
def step_when_user_erases_task (context, task_name):
    """Erase the task with the given name"""
    context.task_manager.remove_task(task_name)  #Erase task using task manager


@then('the task "{task_name}" should not be present in the task list')
def step_then_task_not_in_list(context, task_name):
    """Check that the erased task is not in the list of tasks anymore"""
    tasks = context.task_manager.get_all_tasks() #Retrieve all tasks
    task_names = [task['name'] for task in tasks]  # Extract all names of the tasks
    assert task_name not in task_names, f"The task '{task_name}' wasn't removed from the list" 