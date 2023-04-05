#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        status = response.read()
        print(response.__dict__.get('headers').get('X-Request-Id'))
