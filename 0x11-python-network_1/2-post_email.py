#!/usr/bin/python3
"""
script that takes in a URL and email sends a POST request to passed URL
"""
from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':
    emaildata = parse.urlencode({'email': argv[2]}).encode('ascii')
    request = Request(argv[1], emaildata)
    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
