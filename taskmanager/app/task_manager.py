# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.


class TaskManager:
    """
    This class manages a list of tasks. It initializes an empty list of tasks.
    """
    def __init__(self):
        """
        Initializes the TaskManager with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task_name, task_description):
        """
        Adds a new task to the list of tasks.
        """
        self.tasks.append({'name': task_name, 'description': task_description})

    def get_all_tasks(self):
        """
        Returns all tasks.
        """
        return self.tasks

    # TODO: GRUPPE 1: Add a method to remove a task from the list of tasks

    def update_task(self, task_name, new_task_name=None, new_task_description=None):
        """
        Updates an existing task's name and/or description.
        :param task_name: The name of the task to update.
        :param new_name: The new name of the task (optional).
        :param new_description: The new description of the task (optional).
        :return: True if the task was updated, False if the task was not found.
        """
        for task in self.tasks:
            if task['name'] == task_name:
                if new_task_name:
                    task['name'] = new_task_name
                if new_task_description:
                    task['description'] = new_task_description
                return True  # Task updated successfully
        return False  # Task not found


    # TODO: GRUPPE 3: Add a method to get a task from the list of tasks

    def clear_tasks(self):
        """
        Clears the list of tasks.
        """
        self.tasks = []