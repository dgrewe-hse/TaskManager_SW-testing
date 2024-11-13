Feature: Remove a task

  Scenario: User removes a task
    Given the user of the task manager application wants to delete an existing task
    And the name of the task to be deleted is "My Task"
    When the user erases the task "My Task" from the list of tasks
    Then the task "My Task" does not exist in the list of tasks anymore
