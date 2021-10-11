#!/usr/bin/python3

"""function to return a list of available attributes and methods"""


def lookup(obj):
    """the function return the attributes and methods of obj"""
    return dir(obj)
