#!/usr/bin/python3
"""
Module 101-add_attribute defines a function
that adds a new attribute to a class if possible
"""


def add_attribute(obj, attr, value):
    """
    Adds a new instance attribute

    Args:
        my_object (object): instance of class object
        attr (str): name of new class attribute
        value (void): value of new attribute
    """
    if '__dict__' in dir(obj):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
