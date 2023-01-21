#!/usr/bin/python3
"""Module base contains the base class of future classes
"""
import csv
import json
import turtle


class Base():
    """
    Defines a base class with a private class attribute

    Attributes:
        __nb_objects (int): alternate id of unidentified instance objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor

        Args:
            id (int): unique id of class instance object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): dict of instances inherited from base
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of an instance
        Args:
            json_string (str): string containing list of instance dictionaries
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns: an instance object with all attributes already set

            Args:
                dictionary (dict): keywords and values of instance attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        if cls.__name__ == "Square":
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string serialization of list_objs to a file

            Args:
                list_objs (list): list of instances that inherit from Base
        """
        filename = f"{cls.__name__}.json"
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(cls.to_dictionary(obj))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(obj_list))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON string deserialization"""
        filename = f"{cls.__name__}.json"
        inst_list = []

        try:
            with open(filename, 'r') as f:
                obj_list = cls.from_json_string(f.read())
            for obj in obj_list:
                inst_list.append(cls.create(**obj))
        except FileNotFoundError:
            pass
        finally:
            return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instance objects and saves to a CSV file

            Args:
                list_objs (list): list of instances that inherit from Base
        """
        filename = f"{cls.__name__}.csv"
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(cls.to_dictionary(obj))

        with open(filename, 'w', newline='') as fv:
            writer = csv.DictWriter(fv, obj_list[0].keys())
            writer.writeheader()
            writer.writerows(obj_list)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a deserialized list of instance objects from a CSV file"""
        filename = f"{cls.__name__}.csv"
        inst_list = []

        try:
            with open(filename, 'r') as fv:
                reader = csv.DictReader(fv)
                obj_list = list(reader)
            for obj in obj_list:
                attr_list = {}
                for name, attr in obj.items():
                    attr_list[name] = int(attr)
                inst_list.append(cls.create(**attr_list))
        except FileNotFoundError:
            pass
        finally:
            return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares

            Args:
                list_rectangles (list): list of Rectangle objects to draw
                list_squares (list): list of Square objects to draw
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#33ffff")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#800000")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#660066")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
        turtle.done()
