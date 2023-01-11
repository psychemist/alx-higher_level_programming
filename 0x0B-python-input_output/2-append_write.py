#!/usr/bin/python3
"""
Module 2-append_write
Defines a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    Args:
        filename (string): target file in directory
        text (string): data to be written into file

    Returns:
        (int): number of characters added to stdout
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
