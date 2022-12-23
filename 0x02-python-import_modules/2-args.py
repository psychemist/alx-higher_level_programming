#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
else:
    if len(argv) == 2:
        print("1 argument:")
    else:
        print(f"{len(argv)-1} arguments:")
    for i in range(len(argv)):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, str(argv[i])))
