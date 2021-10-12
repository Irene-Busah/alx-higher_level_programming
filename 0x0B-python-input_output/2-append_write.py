#!/usr/bin/python3

"""The function appends a string at the end of a text file
and returns the number of characters"""


def append_write(filename="", text=""):
    """the function accepts a filename and text as parameters"""
    with open(filename, "a") as file:
        return file.write(text)
