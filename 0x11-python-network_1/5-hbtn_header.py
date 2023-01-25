#!/usr/bin/python3
"""
take url and send request to the url and
display its value of the variable in the response header
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    request = get(argv[1])
    print(request.headers.get("X-Request-Id"))
