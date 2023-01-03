#!/usr/bin/python3
"""
Module 9-rectangle.py
Defines a rectangle based on 8-rectangle.py
"""


class Rectangle:
    """
    Defines a rectangle class with a public class attributes,
    private instance attributes, and public instance methods

    Attributes:
        width (int): length of shorter side of rectangle
        height (int): length of longer side of rectangle
        number_of_instances (int): counter for tracking Rectangle instances
        print_symbol (str): symbol for Rectangle instance string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance object

        Args:
            width (int): defaults to 0 if none
            height (int): defaults to 0 if none
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns: width of Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns: height of Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns:
            int: area of Rectangle instance object
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Returns:
            int: perimeter of Rectangle instance object
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Retruns: new string object from Rectangle instance object
        """
        string = ""

        if self.width == 0 or self.height == 0:
            return string
        else:
            string += "\n".join([str(self.print_symbol) * self.width
                                 for row in range(self.height)])
        return string

    def __repr__(self):
        """
        Returns: canonical string representation of Rectangle instance object
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints an exit message when a Rectangle instance object is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        return self.area == other.area

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return self.area != other.area

    def __lt__(self, other):
        """
        Compares and returns if lesser than
        """
        return self.area < other.area

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        return self.area <= other.area

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.area > other.area

    def __ge__(self, other):
        """
        Compares two Rectangle instance objects based on area

        Returns:
            bool: True if self is greater than/equal to other, False otherwise
        """
        if self.area >= other.area:
            return self
        else:
            return other
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangle instance objects

        Returns:
            Bigger Rectangle instance based on area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        """if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2"""

        return rect_1 > rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square from Rectangle class

        Returns:
            new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)
