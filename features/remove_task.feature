Feature: Remove a task

  Scenario: User removes a task
    Given the user is within the task manager application
    And a task with the name "Task to be erased" is in the task list
    When the user erases the task with the name "Task to be erased"
    Then the task "Task to be erased" should not be present in the task list