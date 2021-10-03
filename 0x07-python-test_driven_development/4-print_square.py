#!/usr/bin/python3

"""The function prints a square with the character # """


def print_square(size):
    """Size is the length of the square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if float(size) < 0:
        raise TypeError("size must be an integer")
    for row in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print("")
    if size == 0:
        print("", end="")
