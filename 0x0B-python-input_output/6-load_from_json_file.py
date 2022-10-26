#!/usr/bin/python3
"""
Module load_from_json_file
It creates an object from a json file
"""


def load_from_json_file(filename):
    """
    i need the json module since it is an external source.
    Argument:

        filename-contain the json
    """
    import json

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
        f.close()
