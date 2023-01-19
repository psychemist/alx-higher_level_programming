#!/usr/bin/python3
"""Module square inherits from Rectangle class defined in rectangle module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class with private instance attributes
    and public instance methods

    Attributes:
        __size (int): private instance attribute representing length
        __x (int): private instance attribute representing x-coordinate
        __y (int): private instance attribute representing y-coordinate
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a new Square instance object

        Args:
            size (int): length of each side of square
            x (int): horizonal position of object instance along x-axis
            y (int): vertical position of object instance along y-axis
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Sqaure instance object"""
        string1 = f"[{self.__class__.__name__}] ({self.id}) "
        string2 = f"{self.x}/{self.y} - {self.width}"
        string = string1 + string2
        return string
