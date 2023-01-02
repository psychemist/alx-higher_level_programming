#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and public area
Can access and update size
Can print to stdout the square using #'s
"""


class Square:
    """
    Instantiates square object with public instance methods, a private
    instance attribute, and getter and setter properties for accessing
    and updating hidden values.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance

        Args:
            size (int): Length of sides of square
            position (tuple): Tuple of two positive integers

        """
        self.size = size  #: size (int): length of square
        self.position = position
        """position(int, int): tuple of two +ve int"""

    def __str__(self):
        """
        String representation of the square objects called by print function
        """
        string = ""
        if self.__size == 0:
            return string
        else:
            string += "\n" * self.__position[1]
            string += "\n".join([" " * self.__position[0] +
                                 "#" * self.__size
                                 for row in range(self.__size)])
        return string

    @property
    def size(self):
        """
        Attribute:
            size (int): read-write property
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Attribute:
            position (tuple): read-write property
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of a square

        Returns:
            int: Area of the square

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square instance with the # character
        or nothing if size is 0
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for row in range(self.__size)]))
