Feature: Remove a task

  Scenario: User removes a task
    Given the user is within the task manager application and the user defines one task as irrelevant
    When the user erases the task
    Then the task disappears from the task list