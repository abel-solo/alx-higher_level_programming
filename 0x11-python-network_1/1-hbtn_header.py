#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL and displays the value of x-requested-id
"""

from sys import argv
from urllib.request import Request
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]

    request = Request(url)
    with urlopen(request) as res:
        print(dict(response.header).get("x-Request-Id"))
