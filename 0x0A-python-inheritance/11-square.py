#!/usr/bin/python3
"""Module 11-square contains a class based on a class in 9-rectangle
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

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the Square instance object
        """
        return (self.__size ** 2)

    def __str__(self):
        """Returns string representation of Square instance object
        """
        string = "[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size)
        return string
