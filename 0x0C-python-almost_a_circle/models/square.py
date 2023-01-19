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

    @property
    def size(self):
        """Returns: length of Square instance"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of Sqaure instance object"""
        string1 = f"[{self.__class__.__name__}] ({self.id}) "
        string2 = f"{self.x}/{self.y} - {self.width}"
        string = string1 + string2
        return string

    def update(self, *args, **kwargs):
        """Assigns an argument to each Square instance attribute"""
        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for num in range(len(args)):
                setattr(self, attrs[num], args[num])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance"""
        dicto = {'id': self.id, 'size': self.size,
                 'x': self.x, 'y': self.y}
        return dicto
