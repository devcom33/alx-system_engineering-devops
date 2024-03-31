#!/usr/bin/python3

"""given employee ID, returns information
about his/her TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    total = 0
    completed = 0
    for i in todos.json():
        if i.get('userId') == int(userId):
            total += 1
            if i.get('completed') is True:
                completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
