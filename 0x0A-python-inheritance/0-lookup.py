#!/usr/bin/python3
"""
Module Lookup
This module retuens the list of available attributes and methodsa of an object.
"""


def lookup(obj):
    """
    return list of attributes and methods
    obj -theobject to look into
    """
    return dir(obj)
