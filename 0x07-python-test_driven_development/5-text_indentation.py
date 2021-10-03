#!/usr/bin/python3

"""The function prints a text with 2 new lines after each
of these characters: '.', '?' and ':'"""


def text_indentation(text):
    """ It takes one parameter and must be a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    var_1 = 1
    for l in text:
        if var_1 == 1 and l == " ":
            pass
        else:
            print(l, end="")
            var_1 = 0
        if l == '.' or l == '?' or l == ':':
            print("\n")
            var_1 = 1
