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

@app.route("/tasks", methods=["DELETE"])
def clear_all_tasks():
    # delete all tasks
    task_manager.clear_tasks()
    # return to user that delete was succesful
    return jsonify({"message":"All tasks were deleted succesfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
