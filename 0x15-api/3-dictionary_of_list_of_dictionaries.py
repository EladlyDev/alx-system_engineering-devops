#!/usr/bin/python3
""" for a given employee ID, returns information
about his/her TODO list progress. from api """
import json
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    prog = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    out = 'todo_all_employees.json'

    all_data = {}
    for user in users:
        data = {user['id']: []}
        tasks = [task for task in prog if task['userId'] == user['id']]
        done = [task for task in tasks if task['completed']]
        username = user['username']
        for task in tasks:
            data[user['id']].append({'username': username,
                                     'task': task['title'],
                                     'completed': task['completed']})
        all_data.update(data)

    with open(out, 'w') as f:
        f.write(json.dumps(all_data))
