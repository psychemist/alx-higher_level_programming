#!/usr/bin/python3
"""
Module 2-matrix_divided
Defines a function that 
"""

"""matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats

Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size


All elements of the matrix should be divided by div, rounded to 2 decimal places

Returns a new matrix
"""
def matrix_divided(matrix, div):
    """
    """
#    if type

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[num / div for num in row] for row in matrix]
