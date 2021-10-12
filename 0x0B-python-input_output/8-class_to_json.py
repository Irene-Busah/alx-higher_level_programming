#!/usr/bin/python3

"""The function returns a dictionary description with simple data structure"""

import json


def class_to_json(obj):
    """Returns a dictionary"""
    json_Str = obj.__dict__
    return json_Str
