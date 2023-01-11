#!/usr/bin/python3
"""
Module 1-write_file
Defines a function that writes a string to a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    Args:
        filename (string): target file in directory
        text (string): data to be written into file

    Returns:
        (int): number of characters written to stdout
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
