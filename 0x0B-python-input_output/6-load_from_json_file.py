#!/usr/bin/python3
"""
Module 6-load_from_json_file
Defines a function that deserializes an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file

    Args:
        my_obj (object): deserialized data structure
        filename (string): JSON file in directory to retrieve object
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.load(my_file)
