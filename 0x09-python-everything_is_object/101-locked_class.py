#!/usr/bin/python3
"""
Module lockedclass
Defines a locked class
"""


class LockedClass:
    """
    Prevents user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']

    def __init__(self, first_name="None"):
        """
        Instantiates new LockedClass object
        """
        if first_name is not None:
            self.first_name = first_name
