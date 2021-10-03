#!/usr/bin/python3

"""The function returns an integer: addition of 'a' and 'b'
a and b must be an integer or a float
"""


def add_integer(a, b=98):
    """the function accepts two parameters"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
