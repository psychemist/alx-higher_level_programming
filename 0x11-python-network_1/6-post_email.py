#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
