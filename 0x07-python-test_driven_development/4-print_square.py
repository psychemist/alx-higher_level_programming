#!/usr/bin/python3
"""
Module 4-print_square
Defines a function that prints a square of specified size
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size == 0:
        print()
    else:
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print()
