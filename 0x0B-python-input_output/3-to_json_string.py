#!/usr/bin/python3
"""
Module 3-to_json_string
Defines a function that serializes an object
"""
import json


def to_json_string(my_obj):
    """
    Serializes a Python object into a JSON string

    Args:
        my_obj (object): data to be serialized

    Returns:
        JSON representation of an object (string)
    """
    return json.dumps(my_obj)
