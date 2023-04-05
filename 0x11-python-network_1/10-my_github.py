#!/usr/bin/python3
'''
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/users/" + argv[1]
    headers = {'Authorization': 'token ' + argv[2]}

    r = requests.get(url, headers=headers)
    print(r.json().get('id'))
