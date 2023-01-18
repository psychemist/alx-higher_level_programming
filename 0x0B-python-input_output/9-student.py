#!/usr/bin/python3
"""
Module 9-student contains a class that retrieves
a JSON serialization of its attributes
"""


class Student:
    """Defines a class with public instance attributes and a public method
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates each instance object with three
        public instance attributes and a public method

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            Dictionary representation of a Student instance object
        """
        return self.__dict__ 
