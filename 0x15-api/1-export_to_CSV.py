#!/usr/bin/python3
"""Exports data from the first script to CSV
"""

import csv
import requests
import sys


def export_user_tasks_to_csv(employee_id):
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
    user_data = user_response.json()
    user_id = user_data.get('id')
    user_name = user_data.get('username')

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
    todos_data = todos_response.json()

    csv_file_name = "{}.csv".format(employee_id)
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        writer.writerow([
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'
            ])

        for todo in todos_data:
            writer.writerow({
                str(user_id),
                user_name,
                str(todo['completed']),
                todo['title']
            })


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    export_user_tasks_to_csv(employee_id)
