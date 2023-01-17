#!/usr/bin/python3

"""
script takes in a url and sends a request to the url and displays the value of variable found in the header of the response
"""

from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
