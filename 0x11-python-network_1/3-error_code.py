#!/usr/bin/python3
""" script that takes in a URL sends a request to the URL and displays body """
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as resource:
            print(resource.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code:', error.code)
