#!/usr/bin/python3
'''
takes 2 arguments and prints commits from a
GitHub repository by shaID and author name
'''

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits".
                     format(argv[2], argv[1]))
    for commit in r.json()[0:10]:
        print("{}: {}".
              format(commit.get('sha'),
                     commit.get('commit').get('author').get('name')))
