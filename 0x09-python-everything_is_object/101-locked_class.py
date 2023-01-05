#!/usr/bin/python3
"""
Module lockedclass
Defines a locked class with no class or object attribute
"""


class LockedClass:
    """
    Prevents user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name

    >>> a = LockedClass()
    >>> a.first_name = 'Agu'
    >>> a.first_name
    'Agu'

    >>> a.last_name = 'Obunadike'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """
    __slots__ = ['first_name']

