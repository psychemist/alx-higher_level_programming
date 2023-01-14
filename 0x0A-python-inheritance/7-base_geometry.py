#!/usr/bin/python3
"""
Module 7-base_geometry

Contains a class based on 6-base_geometry
"""


class BaseGeometry():
    """
    Defines a class with public instance methods
    """
    def area(self):
        """
        Raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value  based on attribute name

        Args:
            name (str): name of integer attribute
            value (int): integer value of string attribute
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
