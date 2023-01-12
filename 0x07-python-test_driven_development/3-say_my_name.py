#!/usr/bin/python3
"""
Module 3-say_my_name
Defines a function that prints a string with two supplied arguments
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string using parameters

    Args:
        first_name (str): positional argument
        last_name (str): keyword argument
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
