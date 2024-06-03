#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{url}/users/{employee_id}")
    user = user_response.json()
    employee_name = user.get("name")

    # Fetch TODO list for the employee
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

