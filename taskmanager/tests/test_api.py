# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import unittest
from taskmanager.app.api import app
from taskmanager.app.task_manager import TaskManager


class APITestCase(unittest.TestCase):
    """
    Unit tests for the TaskManager API.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the Flask application for testing."""
        cls.app = app.test_client()
        cls.app.testing = True
        cls.task_manager = TaskManager()

    def test_add_task_valid(self):
        """Test adding a valid task."""
        response = self.app.post("/tasks", json={"name": "Task 1", "description": "Description 1"})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Task created successfully", response.data)

    def test_add_task_invalid_empty_name(self):
        """Test adding a task with an empty name."""
        response = self.app.post("/tasks", json={"name": "", "description": "Description 1"})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Name is required", response.data)

    def test_add_task_invalid_none_name(self):
        """Test adding a task with None as name."""
        response = self.app.post("/tasks", json={"name": None, "description": "Description 1"})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Name is required", response.data)

    def test_remove_task_valid(self):
        """Test removing an existing task."""
        self.app.post("/tasks", json={"name": "Task 1", "description": "Description 1"})
        response = self.app.delete("/tasks/Task 1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task removed successfully", response.data)

    def test_remove_task_invalid_non_existing(self):
        """Test removing a task that does not exist."""
        response = self.app.delete("/tasks/Non-existing Task")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Task not found", response.data)

    def test_update_task_valid(self):
        """Test updating an existing task."""
        self.app.post("/tasks", json={"name": "Task 1", "description": "Description 1"})
        response = self.app.put(
            "/tasks/Task 1",
            json={"name": "Updated Task", "description": "Updated Description"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task updated successfully", response.data)

    def test_update_task_invalid_non_existing(self):
        """Test updating a task that does not exist."""
        response = self.app.put(
            "/tasks/Non-existing Task",
            json={"name": "Updated Task", "description": "Updated Description"},
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Task with name 'Non-existing Task' not found.", response.data)

    def test_update_task_invalid_empty_new_name(self):
        """Test updating a task with an empty new name."""
        self.app.post("/tasks", json={"name": "Task 1", "description": "Description 1"})
        response = self.app.put(
            "/tasks/Task 1", json={"name": "", "description": "Updated Description"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"New Name is required", response.data)

    def test_clear_tasks(self):
        """Test clearing all tasks."""
        self.app.post("/tasks", json={"name": "Task 1", "description": "Description 1"})
        response = self.app.delete("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All tasks removed successfully", response.data)

    def test_clear_tasks_no_tasks(self):
        """Test clearing tasks when no tasks exist."""
        response = self.app.delete("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All tasks removed successfully", response.data)

    def test_add_task_invalid_description_length(self):
        """Test adding a task with a description longer than 255 characters."""
        long_description = "A" * 256
        response = self.app.post("/tasks", json={"name": "Task 1", "description": long_description})
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b"Name or description cannot be longer than 255 characters", response.data
        )  # Adjust based on actual validation

    def test_update_task_invalid_description_length(self):
        """Test updating a task with a description longer than 255 characters."""
        self.app.post("/tasks", json={"name": "Task 1", "description": "Description 1"})
        long_description = "A" * 256
        response = self.app.put(
            "/tasks/Task 1", json={"name": "Task 1", "description": long_description}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b"New Name or description cannot be longer than 255 characters", response.data
        )  # Adjust based on actual validation


if __name__ == "__main__":
    unittest.main()
