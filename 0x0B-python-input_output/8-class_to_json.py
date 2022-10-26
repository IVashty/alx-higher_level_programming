#!/usr/bin/python3
"""
Module class_to_json
It returns a dictionary description with simple
data Structures for json serialization of an object
"""


def class_to_json(obj):
    """
    Arguments:
        obj-that will be returned as dictionary
    Returns: the dictionary description for JSON
    """
    return obj.__dict__
