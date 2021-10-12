#!/usr/bin/python3

"""The function returns a dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns a dictionary"""

    return obj.__dict__
