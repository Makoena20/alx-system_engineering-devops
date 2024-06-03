#!/usr/bin/python3
"""
Exports tasks owned by an employee to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <USER_ID>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user details
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create JSON structure
    tasks = []
    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks.append(task)

    user_tasks = {user_id: tasks}

    # Write to JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(user_tasks, json_file)

