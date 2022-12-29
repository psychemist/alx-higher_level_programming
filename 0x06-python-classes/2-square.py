#!/usr/bin/python3
"""
Module 2-square
Defines a square based on 1-square.py
"""


class Square:
    """
    Class square instantiation with optional private instance attribute
    """
    def __init__(self, size=0):
        """
        Initializes square

        Args:
            size (int): Length of one side of square
        """
        try:
            if size >= 0:
                self.__size = size
            elif size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
