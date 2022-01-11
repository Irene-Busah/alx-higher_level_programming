#!/usr/bin/python3
"""The script displays the body of the response from a request"""

import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print('Error code: ', request.status_code)
    else:
        print(request.text)
