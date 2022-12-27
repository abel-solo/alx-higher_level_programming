#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
from requests import get

if __name__ == "__main__":
    rs = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rs.text)))
    print("\t- content: {}".format(rs.text))
