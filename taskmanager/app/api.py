# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from flask import Flask, request, jsonify
from task_manager import TaskManager

# initialize Flask app
app = Flask(__name__)

# instanz unseres TaskManagers
task_manager = TaskManager()


# route für alle tasks
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    # return all tasks
    # HTTP status code 200 == OK
    return jsonify(task_manager.get_all_tasks()), 200


@app.route("/tasks", methods=["POST"])
def add_task():
    # get data from request
    data = request.get_json()
    # extract name and description from data
    name = data.get("name")
    description = data.get("description")

    # check if name and description are valid
    if not name:
        return jsonify({"error": "Name is required"}), 400

    # add task to task manager
    task_manager.add_task(name, description)
    # return to user that creation was successful
    # return HTTP status code 201 == Created
    return jsonify({"message": "Task created successfully"}), 201


@app.route("/tasks/<name>", methods=["DELETE"])
def remove_task(name):
    # get data from request
    data = request.get_json()
    # extract name from data
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    # remove task from task manager
    # if task is not found -> task_manager returns False
    if not task_manager.remove_task(name):
        # return HTTP status code 404 == Not Found
        return jsonify({"error": "Task not found"}), 404
    else:
        # return HTTP status code 200 == OK
        return jsonify({"message": "Task removed successfully"}), 200


@app.route("/tasks/<name>", methods=["PUT"])
def update_task(name):
    # get data from request
    data = request.get_json()
    # extract name and description from data
    new_name = data.get("name")
    new_description = data.get("description")

    # check if name and description are valid
    if not new_name:
        return jsonify({"error": "New Name is required"}), 400
    # check if task exists
    if not task_manager.get_task_by_name(new_name):
        return jsonify({"error": "Task not found"}), 404

    # update task in task manager
    task_manager.update_task(name, new_name, new_description)
    # return HTTP status code 200 == OK
    return jsonify({"message": "Task updated successfully"}), 200


@app.route("/tasks", methods=["DELETE"])
def clear_tasks():
    # clear all tasks in task manager
    task_manager.clear_tasks()
    # return HTTP status code 200 == OK
    return jsonify({"message": "All tasks removed successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
