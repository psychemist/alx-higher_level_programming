#!/usr/bin/python3
"""
Module 2-matrix_divided
Defines a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elments of a matrix by a number

    Args:
        matrix (list): list of lists of integers or floats
        div (integer/float): divisor of the equation

    Returns:
        (list): list of floats rounded to 2 places
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(err)
    if not all(isinstance(row, list) for row in matrix) \
       or not isinstance(matrix, list):
        raise TypeError(err)

    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
