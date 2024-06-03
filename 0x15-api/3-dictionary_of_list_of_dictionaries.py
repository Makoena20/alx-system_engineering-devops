#!/usr/bin/python3

"""
This script generates a JSON file containing all tasks from all employees.
"""

import json
from collections import defaultdict

# Define the tasks for each employee
tasks = {
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": False},
        # ... more tasks for user 1
    ],
    "2": [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": True},
        # ... more tasks for user 2
    ],
    "3": [
        {"username": "Samantha", "task": "aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit", "completed": False},
        {"username": "Samantha", "task": "rerum perferendis error quia ut eveniet", "completed": False},
        # ... more tasks for user 3
    ],
    "4": [
        {"username": "Karianne", "task": "odit optio omnis qui sunt", "completed": True},
        {"username": "Karianne", "task": "et placeat et tempore aspernatur sint numquam", "completed": False},
        # ... more tasks for user 4
    ],
    "5": [
        {"username": "Kamren", "task": "suscipit qui totam", "completed": True},
        {"username": "Kamren", "task": "voluptates eum voluptas et dicta", "completed": False},
        # ... more tasks for user 5
    ],
    "6": [
        {"username": "Leopoldo_Corkery", "task": "explicabo enim cumque porro aperiam occaecati minima", "completed": False},
        {"username": "Leopoldo_Corkery", "task": "sed ab consequatur", "completed": False},
        # ... more tasks for user 6
    ],
    "7": [
        {"username": "Elwyn.Skiles", "task": "inventore aut nihil minima laudantium hic qui omnis", "completed": True},
        {"username": "Elwyn.Skiles", "task": "provident aut nobis culpa", "completed": True},
        # ... more tasks for user 7
    ],
    "8": [
        {"username": "Maxime_Nienow", "task": "explicabo consectetur debitis voluptates quas quae culpa rerum non", "completed": True},
        {"username": "Maxime_Nienow", "task": "maiores accusantium architecto necessitatibus reiciendis ea aut", "completed": True},
        # ... more tasks for user 8
    ],
    "9": [
        {"username": "Delphine", "task": "ex hic consequuntur earum omnis alias ut occaecati culpa", "completed": True},
        {"username": "Delphine", "task": "omnis laboriosam molestias animi sunt dolore", "completed": True},
        # ... more tasks for user 9
    ],
    "10": [
        {"username": "Moriah.Stanton", "task": "ut cupiditate sequi aliquam fuga maiores", "completed": False},
        {"username": "Moriah.Stanton", "task": "inventore saepe cumque et aut illum enim", "completed": True},
        # ... more tasks for user 10
    ]
}

# Create a dictionary to store all tasks
all_tasks = defaultdict(list)

# Iterate over each user's tasks
for user_id, user_tasks in tasks.items():
    # Iterate over each task
    for task in user_tasks:
        # Add the task to the all_tasks dictionary
        all_tasks[user_id].append(task)

# Generate the JSON file
with open("todo_all_employees.json", "w") as f:
    json.dump(all_tasks, f, indent=4)


