#!/usr/bin/python3
"""
Module 5-square
Defines a square based on 4-square.py
"""


class Square:
    """
    Instantiates square object with public instance methods, a private
    instance attribute, and getter and setter properties for accessing
    and updating hidden values.
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args: size (int): Length of sides of square

        """
        self.size = size
        """size (int): length of one side of square"""

    @property
    def size(self):
        """int: read-only size property"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of a square

        Returns:
            int: Area of the square

        """
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end="")
                print()
