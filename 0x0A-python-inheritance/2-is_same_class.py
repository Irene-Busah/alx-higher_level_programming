#!/usr/bin/python3

"""The function returns True if the object is exactly an
instance of a specified class
"""


def is_same_class(obj, a_class):
    """Returns True for an object that is an instance of the class specified"""
    if type(obj) == a_class:
        return True
    return False
