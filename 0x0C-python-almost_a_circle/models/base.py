#!/usr/bin/python3
"""Module base contains the base class of future classes
"""
import json


class Base():
    """
    Defines a base class with a private class attribute

    Attributes:
        __nb_objects (int): alternate id of unidentified instance objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor

        Args:
            id (int): unique id of class instance object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): dict of instances inherited from base
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of an instance
        Args:
            json_string (str): string containing list of instance dictionaries
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

            Args:
                list_objs (list): list of instances that inherit from Base
        """
        filename = f"{cls.__name__}.json"
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(cls.to_dictionary(obj))
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(obj_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns: an instance object with all attributes already set

            Args:
                dictionary (dict): keywords and values of instance attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10, 0, 0)
        if cls.__name__ == "Square":
            dummy = cls(10, 0, 0)
        dummy.update(**dictionary)
        return dummy
