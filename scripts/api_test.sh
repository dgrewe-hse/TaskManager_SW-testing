#! /bin/bash

# echo start of script
echo "Start of script"

# test get all tasks
curl -X GET http://127.0.0.1:5000/tasks

# test add task
curl -X POST http://127.0.0.1:5000/task -H "Content-Type: application/json" -d '{"name": "Test Task", "description": "This is a test task."}'

# test update task
curl -X PUT http://127.0.0.1:5000/task/Test%20Task -H "Content-Type: application/json" -d '{"name": "Updated Task", "description": "This is an updated task."}'

# test delete task
curl -X DELETE http://127.0.0.1:5000/task/Updated%20Task

# test add task
curl -X POST http://127.0.0.1:5000/task -H "Content-Type: application/json" -d '{"name": "Test Task", "description": "This is a test task."}'

# test clear all tasks
curl -X DELETE http://127.0.0.1:5000/tasks

# echo end of script
echo "End of script"
