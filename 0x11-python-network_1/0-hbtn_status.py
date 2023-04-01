#!/usr/bin/python3
'''fetches status of a named URL
'''
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()
    print('''Body of response:
    - type: {}
    - content: {}
    - utf8 content: {}'''.
          format(type(status), status, status.decode('utf8')))
