#!/usr/bin/python3

"""
This script generates a JSON file containing all tasks from all employees.
"""

import json
from tasks import tasks

# Create a dictionary to store tasks for each user
tasks_dict = {}

# Iterate over tasks and assign them to users
for user_id, user_tasks in tasks.items():
    tasks_dict[user_id] = []
    for task in user_tasks:
        tasks_dict[user_id].append({
            "username": task["username"],
            "task": task["task"],
            "completed": task["completed"]
        })

# Write tasks to a JSON file
with open("todo_all_employees.json", "w") as f:
    json.dump(tasks_dict, f, indent=4)


