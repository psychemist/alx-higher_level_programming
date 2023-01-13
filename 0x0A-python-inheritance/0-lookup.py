#!/usr/bin/python3
"""
Module 0-lookup

Defines a function that lists the fields and methods of an object
"""


def lookup(obj):
    """
    Lists the available data and method attributes of an object

    Args:
        obj (object): class or instance object 

    Returns:
        (list): list object containing attribute in module namespace
    """
    return obj.__dict__
