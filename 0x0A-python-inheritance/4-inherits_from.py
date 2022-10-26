#!/usr/bin/python3
"""
Module inherits_from
Returns a boolean if the object is an instance of a class inherited from
specified class.
"""


def inherits_from(obj, a_class):
    """
    is the bj an instance of a class be inherits_from a_class
    Arguments:
        obj - object to liik at
        a_class-the class to evaluate
    Return:True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
