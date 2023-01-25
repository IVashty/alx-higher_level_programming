#!/usr/bin/python3
"""
Script that lists the most recent commands
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    v = 0

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = get(url)
    json = response.json()

    for element in json:
        if v > 9:
            break
        k = element.get("k")
        author = element.get("commit").get("author").get("name")
        print("{}: {}".format(k, author))
        v += 1
