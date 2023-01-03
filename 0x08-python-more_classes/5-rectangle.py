#!/usr/bin/python3
"""
Module 4-rectangle.py
Defines a rectangle based on 3-rectangle.py
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
        """Returns: width of rectangle instance"""
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
        """Returns: height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns:
            int: area of rectangle instance object
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Returns:
            int: perimeter of rectangle instance object
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Retruns: new string object from rectangle instance object
        """
        string = ""

        if self.width == 0 or self.height == 0:
            return string
        else:
            string += "\n".join(["#" * self.width
                                 for row in range(self.height)])

        return string

    def __repr__(self):
        """
        Returns: canonical string representation of rectangle instance object
        """
        return f"Rectangle ({self.width}, {self.height})"

    def __del__(self):
        """
        Prints an exit message when a rectangle object instance is deleted
        """
        print("Bye rectangle...")
