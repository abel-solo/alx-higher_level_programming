#!/usr/bin/python3
"""python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import *

if __name__ == "__main__":
    
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        page = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode('utf-8')))
