# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then   

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager

@given('the user is using the task manager application and whats to receive information of an existing task by name')
def step_given_user_is_using_task_manager_application(context):
    """Set up the task manager application for the user."""
    context.task_manager = TaskManager()

@given('a task with name "{task_name}" and description "{task_description}" is managed by the task manager app')
def step_check_if_list_is_empty(context, task_name, task_description):
    # hinzufuegen unserer Task, sodass wir testen können
    context.task_manager.add_task(task_name, task_description)
    
@when('the user requests the task with the specific task name: "{task_name}" and the description "{task_description}"')
def step_when_user_gets_a_task(context, task_name, task_description):
    """Retrieve the task with the given name"""
    context.task = context.task_manager.get_task(task_name)

@then('the task with name "{task_name}" and description "{task_description}" is returned.')
def step_then_user_should_see_a_task(context, task_name, task_description):
    assert context.task is not None
    assert context.task['name'] == task_name
    assert context.task['description'] == task_description