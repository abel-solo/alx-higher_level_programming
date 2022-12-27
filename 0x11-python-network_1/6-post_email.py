#!/usr/bin/python3
"""
given URL & email as params, send POST req to URL, display response body utf-8
"""
from sys import argv
import requests

if __name__ == "__main__":
    req = post(argv[1], {'email': argv[2]})
    print(req.text)
