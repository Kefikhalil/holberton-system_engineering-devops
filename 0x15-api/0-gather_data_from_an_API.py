#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    TASK_TITLE = []
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId)).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId)).json()
    for task in tsks:
        if task.get('completed') is True:
            task_titel.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(TASK_TITLE), len(tsks)))
    for i in TASK_TITLE:
        print("\t {}".format(i))
