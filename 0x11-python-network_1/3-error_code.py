#!/usr/bin/python3
"""
script takes in a url and
displays the body of a response from a url
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as theError:
        print("Error Code:", theError.code)
