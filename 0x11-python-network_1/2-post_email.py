#!/usr/bin/python3
""" script that takes URL and email sends a POST request to passed URL """

from sys import argv
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = argv[1]
    emaildata = {'email': argv[2]}
    data = urllib.parse.urlencode(emaildata).encode('ascii')
    req = urllib.request.Request(url,data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
