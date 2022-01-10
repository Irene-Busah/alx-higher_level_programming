#!/usr/bin/python3
"""The script fetches the body of the response of a URL"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    request = Request('https://intranet.hbtn.io/status')
    with urlopen(request) as response:
        content = response.read()
        UTF8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {_type}".format(_type=type(content)))
        print("\t- content: {_content}".format(_content=content))
        print("\t- utf8 content: {_utf8_c}".format(_utf8_c=UTF8_content))
