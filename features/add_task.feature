Feature: Add a Task

  Scenario: User adds a new task to the task list
    Given the user is using the task manager application for adding a task
    And the name of a new task and the description of the new task is available
    When the user adds a new task with the name "Complete project report" and the description "Complete the project report"
    Then the newly created task should appear in the total list of tasks
