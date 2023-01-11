#!/usr/bin/python3
"""
Module 4-from_json_string.py
Defines a function that deserializes a JSON string
"""
import json


def from_json_string(my_obj):
    """
    Desrializes a JSON string into a Python object

    Args:
        my_obj (object): JSON string to be deserialized

    Returns:
        (object): Python data structure represented by a JSON string:
    """
    return json.loads(my_obj)
