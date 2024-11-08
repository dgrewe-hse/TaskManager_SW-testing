# Task Management Application

## Project Description

This Python application is designed to manage tasks or to-dos in the form of a list. It allows users to perform the following key features:

- **Add a Task**: Users can create a new task with a description. Each task is automatically assigned a unique ID and starts with a status of “not completed.”
- **View All Tasks**: Users can retrieve a complete list of tasks, including details like task ID, description, and completion status, for an easy overview of ongoing tasks.
- **Mark a Task as Completed**: Users can mark tasks as completed using the task’s ID, changing the task’s status from “not completed” to “completed.”
- **Delete a Task**: Users can remove tasks by their ID. Once deleted, a task is permanently removed from the task list.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package installer)

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/MoisesGzz92/TaskManager_SW-testing
   cd TaskManager_SW-testing
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows use
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To ensure the application works as expected, you can run tests using `pytest` and `behave`.

### Running Unit Tests (Pytest)

To run the unit tests with `pytest`, execute the following command in your terminal:

```bash
pytest
```

### Running Behavior-Driven Tests (Behave)

To run the behavior-driven tests with `behave`, execute the following command in your terminal:

```bash
behave
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
