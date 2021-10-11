#!/usr/bin/python3

"""The function returns True if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a_class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
