#!/usr/bin/python3
"""This script returns information about a TODO list
of a all users.
"""

import json
import requests


def get_all_tasks():
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users'
        ).json()

    todos_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
        ).json()

    users = {}
    for user in user_response:
        user_id = user.get('id')
        user_name = user.get('username')
        todo_data = list(
            filter(lambda x: x.get('userId') == user_id, todos_response)
            )
        user_data = list(map(
                lambda x: {
                    "username": user_name,
                    "task": x.get("title"),
                    "completed": x.get("completed")
                },
                todo_data
            ))
        users['{}'.format(user_id)] = user_data

    with open('todo_all_employees.json', 'w') as file:
        json.dump(users, file)


if __name__ == '__main__':
    get_all_tasks()
