#!/usr/bin/python3
"""The script displays the body of the response sent to a URL"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode


if __name__ == "__main__":
    request = Request(argv[1])
    try:
        with urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code: ', err.code)
