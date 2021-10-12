#!/usr/bin/python3
""" Add item and save to a file """
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    py_list = load_from_json_file("add_item.json")
except:
    py_list = []

for e in range(1, len(sys.argv)):
    py_list.append(sys.argv[e])

save_to_json_file(py_list, "add_item.json")
