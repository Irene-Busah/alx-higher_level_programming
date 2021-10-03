#!/usr/bin/python3

"""The function print the name of a person"""


def say_my_name(first_name, last_name=""):
    """The function takes two parameters and prints
    a person's name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
