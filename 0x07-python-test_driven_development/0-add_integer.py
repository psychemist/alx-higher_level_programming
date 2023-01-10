#!/usr/bin/python3
"""
Module 0-add_integer
Defines a function that returns the sum of two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        (int): sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
