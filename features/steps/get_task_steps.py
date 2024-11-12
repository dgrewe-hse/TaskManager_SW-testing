# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then   

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager

# TODO: GRUPPE 3 - Add BDD steps for getting a specific task by name

@given('the user is using the task manager application for looking at or getting a task by name')
def step_given_user_is_using_task_manager_application(context):
    """Set up the task manager application for the user."""
    context.task_manager = TaskManager()

@given('at least one task is available in the list')
def step_check_if_list_is_empty(context):

    context.task_manager.get_all_tasks() == []
    
@when('the user gets a task with a specific task_name "{task_name}"')
def step_when_user_gets_a_task(context, task_name):
    """Retrieve the task with the given name"""
    context.task = context.task_manager.get_task(task_name)

@then('the name and description is returned')
def step_then_user_should_see_a_task(context, task_name):
    assert context.task_manager.get_task(task_name) == context.task_manager.task_name