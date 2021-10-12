#!/usr/bin/python3

"""The function writes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""
    with open(filename, "w") as file:
        obj_1 = json.dumps(my_obj)
        file.write(obj_1)
