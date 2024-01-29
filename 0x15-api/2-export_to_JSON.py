#!/usr/bin/python3
"""Exports data from the first script to CSV
"""

import json
import requests
import sys


def export_user_tasks_to_json(employee_id):
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

    json_file_name = "{}.json".format(employee_id)
    with open(json_file_name, 'w', newline='') as jsonfile:
        user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_name
                    },
                    todos_data
                ))
        user_data = {
            "{}".format(user_id): user_data
        }
        json.dump(user_data, jsonfile)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    export_user_tasks_to_json(employee_id)
