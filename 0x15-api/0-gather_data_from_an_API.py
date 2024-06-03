#!/usr/bin/python3
"""
This script uses a REST API to get information about an employee's TODO list progress.
It accepts an employee ID as a parameter and displays the TODO list progress.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch employee details
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()
        
        # Fetch employee's TODO list
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        
        employee_name = user_data.get('name')
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get('completed')]
        done_tasks_count = len(done_tasks)
        
        # Display the result
        print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")

