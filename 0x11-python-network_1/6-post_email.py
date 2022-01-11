#!/usr/bin/python3
"""The script sends a POST request to a URL and displays the
body of the response"""

import requests
from sys import argv


if __name__ == "__main__":
    load = {'email': argv[2]}
    request = requests.get(argv[1])
    print(request.text)
