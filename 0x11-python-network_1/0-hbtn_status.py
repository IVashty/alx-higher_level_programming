#!/usr/bin/python3
"""
fetch url and give a response status that is provided
"""

from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    myhtml = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(myhtml)))
    print("\t- content: {}".format(myhtml))
    print("\t- utf8 content: {}".format(myhtml.decode("utf-8")))
