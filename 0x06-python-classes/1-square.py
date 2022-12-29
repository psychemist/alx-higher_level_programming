#!/usr/bin/python3
"""
Module 1-square
Defines a square type with a private instance attribute, size
"""


class Square:
    """
    Defines a square based on 0-square
    """
    def __init__(self, size):
        """
        Initializes an instance of the Square class

	Args:
            size (int): length of one side of square
        """
        self.__size = size
