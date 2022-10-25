#!/usr/bin/python3
"""
Module to-json_string
It returns the json representation of the object.
"""


def to_json_string(my_obj):
    """
    We needthe Module JSON
    Argument:
        my_obj -will be coverted to json strig
    """
    from json import dumps

    return dumps(my_obj)
