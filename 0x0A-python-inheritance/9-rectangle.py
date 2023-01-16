#!/usr/bin/python3
"""Module 9-rectangle contains a class based on a class in 8-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiates an instance object

        Args:
            width (int): length of shoter side of rectangle
            height (int): length of longer side of rectangle
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle instance object
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Returns string representation of Rectangle instance object
        """
        string = f"[Rectangle] {self.__width}/{self.__height}"
        return string
