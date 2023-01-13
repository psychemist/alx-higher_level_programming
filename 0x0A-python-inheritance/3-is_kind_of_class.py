#!/usr/bin/python3
"""
Module 3-is_same_class

Defines a function that checks an instance’s type or inheritance
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class or if
    the object is a class instance that inherited from the specified class

    Args:
        obj (object): user defined object instance
        a_class (class): Python in-built class object

    Returns:
        (bool): True if an object instance or False if otherwise
    """
    return isinstance(obj, a_class)
