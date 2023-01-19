#!/usr/bin/python3
"""
fetch given url to find status
"""
import requests


if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.content.decode("utf-8")))
