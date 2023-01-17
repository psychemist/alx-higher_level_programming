#!/usr/bin/python3
"""Module rectangle inherits from the Base class defined in base module
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle class with private instance attribute

    Attributes:
        __width (int): private instance attribute representing width
        __height (int): private instance attribute representing length
        __x (int): private instance attribute representing x-coordinate
        __y (int): private instance attribute representing y-coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantites a new Rectangle instance object

        Args:
            width (int): length of shorter side of Rectangle instance object
            height (int): length of longer side of Rectangle instance object
            x (int): horizontal position of object instance along x-axis
            y (int): vertical position of object instance along y-axis
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns: width of Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Returns: height of Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Returns: x-coordinate of Rectangle instance
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Returns: y-coordinate of Rectangle instance
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
