#!/usr/bin/python3
"""
take url and send request to the url and
display its value of the variable in the response header
"""
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    print(request.headers["X-Request-Id"])
