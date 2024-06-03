#!/usr/bin/python3
"""
Exports to-do list information of a given employee to a CSV file.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    
    # Fetch the user information
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')
    
    # Fetch the tasks information
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Write to CSV file
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csvwriter.writerow([user_id, username, task.get('completed'), task.get('title')])

