Feature: Get a task

  Scenario: User gets a task
    TODO: Add steps for getting a task
  Given the user is using the task manager application for looking at or getting a task by name
  And at least one task is available in the list 
  When the user gets a task with a specific task_name "My Task"
  Then the name and description of "My Task" is returned