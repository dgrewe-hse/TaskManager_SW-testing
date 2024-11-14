Feature: Get a task

  Scenario: User gets a task
    Given the user is using the task manager application and whats to receive information of an existing task by name
    And a task with name "My Task" and description "My Description" is managed by the task manager app
    When the user requests the task with the specific task name: "My Task" and the description "My Description"
    Then the task with name "My Task" and description "My Description" is returned.