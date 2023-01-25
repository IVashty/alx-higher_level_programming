#!/usr/bin/python3
"""
takes in the url,sends a reuest to it(url) and
displays the body of response with requests library
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    error = "Error code: {}"
    status = response.status_code

    print(error.format(status) if (status >= 400) else response.text)
