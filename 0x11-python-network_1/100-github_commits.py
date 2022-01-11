#!/usr/bin/python3
""" Github commits challenge """

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    url = "https://api.github.com/repos/"+repo+"/"+owner+"/commits"
    print("URL:", url)

    try:
        r = requests.get(url).json()
        i = 0

        while (i < 10):
            print(r[i]['sha']+": "+r[i]['commit']['author']['name'])
            i += 1
    except:
        pass
