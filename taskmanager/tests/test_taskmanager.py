# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import unittest
from taskmanager.app.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the TaskManager class.
    """

    # TODO: Implement missing tests

    # * add_task -> gegeben: name NONE -> Exception
    # * add_task -> gegeben: Namen länge mehr als 255 Zeichen, keine description -> Exception
    # * add_task -> gegeben: name, description mehr als 255 Zeichen -> Exception
    # * get_task_by_name -> "" (leer) name -> Exception
    # * get_task_by_name -> NONE für name -> Exception
    # * remove_task -> NONE für name -> Exception
    # * remove_task -> name, der nicht existiert -> Exception
    # * update_task -> NONE für name -> Exception
    # * update_task -> name, "" (leer) new_description -> Exception
    # * update_task -> name, new_description, "" (leer) -> Exception
    # * update_task -> name, der nicht existiert -> Exception

    def setUp(self):
        """
        Set up a TaskManager instance for testing.
        """
        self.task_manager = TaskManager()

    def test_add_task_valid_case(self):
        """
        Test adding a valid task.
        """
        self.task_manager.add_task("Task 1", "Description 1")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_add_task_invalid_empty_name(self):
        """
        Test adding a task with an empty name (boundary case).
        """
        with self.assertRaises(ValueError):
            self.task_manager.add_task("", "Description 1")

    def test_get_all_tasks_empty_case(self):
        """
        Test getting all tasks when the list is empty.
        """
        self.assertEqual(self.task_manager.get_all_tasks(), [])

    def test_get_task_by_name_valid_case(self):
        """
        Test getting a task by name that exists.
        """
        self.task_manager.add_task("Task 1", "Description 1")
        task = self.task_manager.get_task_by_name("Task 1")
        self.assertEqual(task["name"], "Task 1")
        self.assertEqual(task["description"], "Description 1")

    def test_get_task_by_name_invalid_non_existing_case(self):
        """
        Test getting a task by name that does not exist.
        """
        with self.assertRaises(KeyError):
            self.task_manager.get_task_by_name("Non-existing Task")

    def test_remove_task_valid_case(self):
        """
        Test removing a task that exists.
        """
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.remove_task("Task 1")
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_remove_task_invalid_non_existing_case(self):
        """
        Test removing a task that does not exist.
        """
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.remove_task("Non-existing Task")
        self.assertEqual(len(self.task_manager.tasks), 1)  # Should remain unchanged

    def test_update_task_valid_case(self):
        """
        Test updating an existing task.
        """
        self.task_manager.add_task("Task 1", "Description 1")
        updated = self.task_manager.update_task("Task 1", new_task_name="Updated Task 1")
        self.assertTrue(updated)
        task = self.task_manager.get_task("Updated Task 1")
        self.assertEqual(task["description"], "Description 1")

    def test_update_task_invalid_non_existing_case(self):
        """
        Test updating a task that does not exist.
        """
        updated = self.task_manager.update_task("Non-existing Task", new_task_name="Updated Task")
        self.assertFalse(updated)

    def test_clear_tasks_case(self):
        """
        Test clearing all tasks.
        """
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.clear_tasks()
        self.assertEqual(len(self.task_manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
