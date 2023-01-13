#!/usr/bin/python3
"""
Module 4-inherits_from

Defines a function that checks an instance’s inheritance
"""


def inherits_from(obj, a_class):
    """
    Checks if an object instance inherited (directly or indirectly)
    from the specified class

    Args:
        obj (object): user defined object instance
        a_class (class): Python in-built class object

    Returns:
        (bool): True if an object instance or False if otherwise
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
