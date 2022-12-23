#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for grid in matrix:
        for num in grid:
            print("{:d} ".format(num), end="")
        print()
