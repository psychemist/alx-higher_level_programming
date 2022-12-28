#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        res = None
    return res
