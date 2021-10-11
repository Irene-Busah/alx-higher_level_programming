#!/usr/bin/python3

"""The function returns True if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the obj is an instance of the a_class"""
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    return False
