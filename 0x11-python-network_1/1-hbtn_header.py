#!/usr/bin/python3
"""
sends a request to the URL and displays the value of x-requested-id
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(res.getheader("x-Request-Id"))
