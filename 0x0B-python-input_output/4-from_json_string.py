#!/usr/bin/python3
"""
Module from_json_string
It returns an python object represented by a JSON string
"""


def from_json_string(my_str):
    """
    Imort JSON since it is an external source.
    Argument:
        my_str-converts to a py file
    Returns : a python objet
    """
    from json import loads

    return loads(my_str)
