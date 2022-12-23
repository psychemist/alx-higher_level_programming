#!/usr/bin/python3
from sys import argv

args = argv[1:]
size = len(args)
if __name__ == '__main__':
    print("{:d} {:s}{:s}".format(size,
                                 "argument" if size == 1 else "arguments",
                                 "." if size == 0 else ":"))
    for idx, arg in enumerate(args):
        print("{:d}: {:s}".format(idx + 1, arg))
