#!/usr/bin/python3
"""
Script that lists the most recent commands
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{owner_name}/{repo_name}"

    # make a get request to the url
    response = get(url)
    # extract from the json
    json = response.json()
    print("The repository {owner_name}/{repo_name} has {json} json.")
