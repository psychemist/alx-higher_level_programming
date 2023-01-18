#!/usr/bin/python3
"""Module rectangle inherits from the Base class defined in base module
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle class with private instance attribute
    and public instance methods

    Attributes:
        __width (int): private instance attribute representing width
        __height (int): private instance attribute representing length
        __x (int): private instance attribute representing x-coordinate
        __y (int): private instance attribute representing y-coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates a new Rectangle instance object

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns: height of Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns: x-coordinate of Rectangle instance
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns: y-coordinate of Rectangle instance
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """Returns string representation of Rectangle instance object
        """
        string1 = f"[{self.__class__.__name__}] ({self.id}) "
        string2 = f"{self.x}/{self.y} - {self.width}/{self.height}"
        string = string1 + string2
        return string

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Prints in stdout the Rectangle instance with the '#' character"""
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.width
                         for row in range(self.height)]))
