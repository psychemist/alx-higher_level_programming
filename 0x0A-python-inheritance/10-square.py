#!/usr/bin/python3
"""Module 10-square contains a class based on a class in 9-rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiates an instance object

        Args:
            size (int): length of all sides of the square
        """

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the Square instance object
        """
        return (self.__size ** 2)

    def __str__(self):
        """Returns string representation of Rectangle instance object
        """
        string = f"[Rectangle] {self.__size}/{self.__size}"
        return string
