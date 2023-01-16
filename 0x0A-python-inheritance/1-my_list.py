#!/usr/bin/python3
"""Module that contains a list class instance
"""


class MyList(list):
    """Defines a class object that inherits from Python list object
       and has a public instance method
    """
    def print_sorted(self):
        """Prints the list but sorted in ascending order
        """
        print(sorted(self))
