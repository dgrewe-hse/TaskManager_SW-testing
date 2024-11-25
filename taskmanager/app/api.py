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

@app.route("/tasks/<string:task_name>", methods=["PUT"])
def update_task(task_name):
    # get data from request
    data = request.get_json()

    # extract name and description from data
    new_name = data.get("new_name")
    new_description = data.get("new_description")

    # check if name and description are valid
    if not new_name and not new_description:
        return jsonify({"error": "At least one field (new_name or new_description) must be provided"}), 400
    
    # check if the task exists
    task = task_manager.get_task_by_name(task_name)
    if not task:
        return jsonify({"error": f"Task with name '{task_name}' not found"}), 404
    
    # call TaskManager's update_task method
    task_manager.update_task(
        task_name, 
        new_task_name=new_name, 
        new_task_description=new_description
    )
    # return success message
    return jsonify({"message": "Task updated successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
