#!/usr/bin/python3
"""
Module 1-rectangle.py
Defines a rectangle based on 0-rectangle.py
"""


class Rectangle:
    """
    Defines a rectangle class with private instance attributes
    and public instance methods

    Attributes:
        width (int): length of shorter side of rectangle
        height (int): length of longer side of rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance object

        Args:
            width (int): defaults to 0 if none
            height (int): defaults to 0 if none
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns: width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return: height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
