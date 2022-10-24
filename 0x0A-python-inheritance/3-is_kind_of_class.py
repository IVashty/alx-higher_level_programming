#!/usr/bin/python3
"""
Module is_kind_of_class
It returns a boolean if the module is an instance of, or if the object is
an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Arguments:
    obj && a_class
    returns TRUE if the module is an instance of , or if the objet is an
    instance of that class that inherited from the speciified class otherwise
    return FALSE.
    """
    return isinstance(obj, a_class)
