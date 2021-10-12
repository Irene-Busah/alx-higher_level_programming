#!/usr/bin/python3

"""The function creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, "w") as file:
        return json.loads(file.readline())
