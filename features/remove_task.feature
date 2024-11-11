Feature: Remove a task

  Scenario: User removes a task
    Given the user is within the task manager application
    And the name of the irrelevant task is available
    When the user erases the task with the name "Task to be erased"
    Then the task disappears from the task list