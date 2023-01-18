#!/usr/bin/python3
"""
Module 10-student contains a class that retrieves
a filtered JSON serialized list of its attributes
"""


class Student:
    """Defines a class with public instance attributes and a public method
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates each instance object with three
        public instance attributes and a public method

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns:
            Dictionary representation of a Student instance object
        """
        attr_dict = {}
        if attrs is not None:
            for attr in attrs:
                if attr in self.__dict__:
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict
        return self.__dict__
