#!/usr/bin/python3
""" script that takes URL and email sends a POST request to passed URL """
from sys import argv
from urllib import parse
from urllib.request import Request, urlopen

if __name__ == '__main__':
    email = parse.urlencode({'email': argv[2]}).encode('ascii')
    request = Request(argv[1], email)
    with urlopen(request) as resource:
        print(resource.read().decode('utf-8'))
