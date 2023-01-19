#!/usr/bin/python3
"""
takes in the url,sends a reuest to it(url) and
displays the body of response with requests library
"""
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code == requests.codes.ok:
        print(request.text)
    else:
        print("Error Code: {}", request.status_code)
