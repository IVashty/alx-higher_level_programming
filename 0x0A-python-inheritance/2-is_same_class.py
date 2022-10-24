#!/usr/bin/python3
"""
Module is_same_class
Cheks TRUE if the object is exactly an instance of the specified clas.
"""


def is_same_class(obj, a_class):
    """
    finds ot if the object is the same class of a_class
    Arguments:
    obj && a_class
    returns a booleanTTrue othrwie False
    """
    return True if type(obj) == a_class else False
