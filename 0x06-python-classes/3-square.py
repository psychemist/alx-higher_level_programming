#!/usr/bin/python3
"""
Module 3-square
Defines a square based on 2-square.py
"""


class Square:
    """
    Instantiates square object with public and private attributes
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args: size (int): Length of sides of square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  #: int: Private instance attribute

    def area(self):
        """Calculates the area of a square

        Returns:
            int: Area of the square

        """
        return self.__size ** 2
