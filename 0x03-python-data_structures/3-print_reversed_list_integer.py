#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        if my_list is None:
            return
        else:
            print("{:d}".format(num))
