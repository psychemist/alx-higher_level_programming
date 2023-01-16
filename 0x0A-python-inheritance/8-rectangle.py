#!/usr/bin/python3
"""Module 8-rectangle contains a class based on a class in 7-base_geometry
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
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
