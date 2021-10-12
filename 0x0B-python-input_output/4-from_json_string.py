#!/usr/bin/python3

"""The function returns an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """the functions accepts a json string"""
    return json.loads(my_str)
