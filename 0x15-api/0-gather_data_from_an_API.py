#!/usr/bin/python3

import requests
import sys

userId = sys.argv[1]
user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
name = user.json().get('name')
print("-----------------------------------------------")
todos = requests.get('https://jsonplaceholder.typicode.com/todos')

total = 0
completed = 0
for i in todos.json():
    if i.get('userId') == int(userId):
        total += 1
        if i.get('completed') is True:
            completed += 1
print("Employee {} is done with tasks({}/{}):".format(name, completed, total))
