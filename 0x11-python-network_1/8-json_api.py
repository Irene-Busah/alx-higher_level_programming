#!/usr/bin/python3
"""The script takes a letter and sends a POST request to a URL"""

import requests
from sys import argv


if __name__ == "__main__":
    json_dict = {}
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        json_dict['q'] = ""
    elif len(argv) == 2:
        json_dict['q'] = argv[1]

    r = requests.post(url, json_dict)
    try:
        json_rep = r.json()
        if bool(json_rep) is False:
            print("No result")
        else:
            print("[{}] {}".format(json_rep['id'], json_rep['name']))
    except:
        print("Not a valid JSON")

