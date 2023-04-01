#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response
'''
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        status = response.read()
        print(response.__dict__.get('headers').get('X-Request-Id'))
