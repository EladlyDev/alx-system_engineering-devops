#!/usr/bin/python3
""" for a given employee ID, returns information
about his/her TODO list progress. from api """
import json
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    prog = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    tasks = [task for task in prog if str(task['userId']) == argv[1]]
    done = [task for task in tasks if task['completed']]
    out = '{}.json'.format(argv[1])

    name = ''
    username = ''
    for user in users:
        if argv[1] == str(user['id']):
            name = user['name']
            username = user['username']
            break

    data = {argv[1]: []}
    for task in tasks:
        data[argv[1]].append({'task': task['title'],
                              'completed': task['completed'],
                              'username': username})

    with open(out, 'w') as f:
        f.write(json.dumps(data))
