#!/usr/bin/python3
""" for a given employee ID, returns information
about his/her TODO list progress. from api """
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    prog = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    tasks = [task for task in prog if str(task['userId']) == argv[1]]
    done = [task for task in tasks if task['completed']]

    name = ''
    for user in users:
        if argv[1] == str(user['id']):
            name = user['name']
            break

    print('Employee {} is done with tasks({}/{}):'.format(name, len(done),
                                                          len(tasks)))
    for task in done:
        print('\t {}'.format(task['title']))
