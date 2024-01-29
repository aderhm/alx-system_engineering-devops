#!/usr/bin/python3
"""This script returns information about a TODO list progress
of a given user (ID)
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))
    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
