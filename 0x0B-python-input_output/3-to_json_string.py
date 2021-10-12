#!/usr/bin/python3

"""The function returns a JSON representation"""

import json


def to_json_string(my_obj):
    """the function accepts an object as a parameter"""
    return json.dumps(my_obj, sort_keys=True)
