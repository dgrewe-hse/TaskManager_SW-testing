# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager

# TODO: GRUPPE 1 - Add BDD steps for removing a task

	
@given('the user is using the task manager application and the user defines one task as irrelevant')
def step_given_user_is_using_task_manager_application(context):
    """Set up the task manager application for the user."""
    context.task_manager = TaskManager()

@when('the user erases the task')
def step_when_user_erases_task (context, task_name):
    context.taskmanager.erase_task()

@then('the task should disappear from the task list')
def step_when_the_task_disappears_from_the_list(context,task_name):
    assert context.taskmanager.get_task-ID() == """Task does not exist"""