#!/usr/bin/python3

"""The function divides all elements of a matrix
and return a new matrix"""


def matrix_divided(matrix, div):
    """The function accepts two parameters"""
    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for element in matrix:
        if not matrix:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if type(element) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for element2 in element:
            if not element:
                raise("matrix must be a matrix (list of lists) \
of integers/floats")
            if type(element2) not in[int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

    new_list = [[round(element2 / div, 2) for element2 in element] for
                element in matrix]
    return new_list
