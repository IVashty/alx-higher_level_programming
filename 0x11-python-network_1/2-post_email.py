#!/usr/bin/python3

"""
script takes in a url and email,
then sends a post request to the passed URL with thw email as return parse
and displaysthe body ofthe response decode in utf8
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    emailpassed = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], emailpassed) as response:
        print(response.read().decode("utf-8"))
