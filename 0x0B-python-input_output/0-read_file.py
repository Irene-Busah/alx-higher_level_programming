#!/usr/bin/python3

"""reads the content of a file and prints to stdout"""


def read_file(filename=""):
    """The function accepts a filename"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
