#!/usr/bin/python3
""" for a given employee ID, returns information
about his/her TODO list progress. from api """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    prog = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    tasks = [task for task in prog if str(task['userId']) == argv[1]]
    done = [task for task in tasks if task['completed']]
    out = '{}.csv'.format(argv[1])

    name = ''
    username = ''
    for user in users:
        if argv[1] == str(user['id']):
            name = user['name']
            username = user['username']
            break

    with open(out, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([argv[1], username, task['completed'],
                            task['title']])
