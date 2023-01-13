#!/usr/bin/python3
"""
Module 2-is_same_class

Defines a function that checks an instance’s type
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj (object): user defined object instance
        a_class (class): Python in-built class object

    Returns:
        (bool): True if an object instance or False if otherwise
    """
    return type(obj) == a_class
