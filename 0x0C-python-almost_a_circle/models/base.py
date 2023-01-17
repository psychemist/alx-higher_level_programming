#!/usr/bin/python3
"""Module base contains the base class of future classes
"""


class Base():
    """
    Defines a base class with a private class attribute

    Attributes:
        __nb_objects (int): alternate id of unidentified instance objects 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class constructor

        Args:
            id (int): unique id of class instance object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__class__.__nb_objects

