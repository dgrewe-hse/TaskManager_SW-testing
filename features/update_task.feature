Feature: Update a task

  Scenario: User updates a task
    Given the user is using the task manager application for updating a task
    And a task is existing in the total list of tasks with the name "Complete project report" and the description "Complete the project report"
    When the user updates the existing task with the name "Changed Complete project report" and the description "Changed Complete the project report"
    Then the changed task should appear updated in the total list of tasks
    