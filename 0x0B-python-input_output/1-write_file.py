#!/usr/bin/python3

"""the function writes a string to a text file"""


def write_file(filename="", text=""):
    """The function accepts a filename and text as parameters"""
    with open(filename, 'w') as file:
        return file.write(text)
