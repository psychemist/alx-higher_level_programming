#!/usr/bin/python3
'''
sends a POST request to http://0.0.0.0:5000/search_user
using an accepted argument as a parameter
'''

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        num = argv[1]
    else:
        num = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': num})

    try:
        res = r.json()
        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
