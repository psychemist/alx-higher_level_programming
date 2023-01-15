#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints out a modified text string
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text (str): text to be modified
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ['.', ':', '?']:
        text = text.replace(char, char + "\n\n")
    text_list = [line.strip(' ') for line in text.split('\n')]
    text_lines = '\n'.join(text_list)
    print(text_lines)
