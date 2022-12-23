#!/usr/bin/python3
from sys import argv

args = argv[1:]
size = len(argv)

if __name__ == '__main__':
    total = 0
    for arg in args:
        total += int(arg)
print(total)
