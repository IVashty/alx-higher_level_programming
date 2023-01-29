#!/usr/bin/python3
"""
script takes in a url and
displays the body of a response from a url
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as Error:
        print("Error Code:", Error.code)
