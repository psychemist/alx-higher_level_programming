#!/usr/bin/python3
"""
Module 0-read_file
Defines a function that prints out a file's contents
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (string): file in directory to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
