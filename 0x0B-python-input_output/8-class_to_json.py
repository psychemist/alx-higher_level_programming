#!/usr/bin/python3
"""Module 8-class_to_json r
"""


def class_to_json(obj):
    """
    Returns public attributes of an instance
    object in a dictionary representation

    Args:
        obj (object): class instance to be serialized

    Returns:
        Dictionary description with simple data structure
        for JSON serialization of an object:
    """
    attrs = {}
    for name in obj.__dict__:
        if name[0] != "_":
            attr = getattr(obj, name)
            attrs[name] = attr
    return attrs

    """
    Alternatively:
        return {name: attr for name, attr in obj.__dict__.items()
                          if not name.startswith("__")}
    """
