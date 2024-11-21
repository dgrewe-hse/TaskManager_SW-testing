Feature: Get all tasks

  Scenario: User gets all tasks
    Given the user is using the task manager application for getting all tasks
    When the user gets all tasks
    Then the user should see all tasks
