#!/usr/bin/python3
"""Module 100-my_int contains a class that inherits from int
"""


class MyInt(int):
    """Defines a class that inherits from int object but with reversed equality
    """
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        """
        Compares and returns if NOT EQUAL
        """
        return self.num != other

    def __ne__(self, other):
        """
        Compares and returns if EQUAL
        """
        return self.num == other
