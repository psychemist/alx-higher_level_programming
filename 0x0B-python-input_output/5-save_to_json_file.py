#!/usr/bin/python3
"""
Module 5-save_to_json_file
Defines a function that serializes an object and writes it into a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using a JSON representation:

    Args:
        my_obj (object): data structure to be serialized
        filename (string): file in directory to be written to
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
