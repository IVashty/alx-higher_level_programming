#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""

from requests import post
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1] if len(argv) >= 2 else ""}
    response = post(url, data)

    type_res = response.headers["content-type"]

    if type_res == "application/json":
        result = response.json()
        _id = result.get("id")
        name = result.get("name")
        if result != {} and _id and name:
            print("[{}] {}".format(_id, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
