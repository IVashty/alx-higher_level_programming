#!/usr/bin/python3
"""
Module name is  add-integer
it adds two integer  a and b
If the input is  a float it automatically changes to an integer.
"""


def add_integer(a, b=98):
    """
    add_integer
    first it will check if the input is correct.
    It should turn it to automaticaly to an integer then adds the integers.
    """
    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError("a must be an integer")
        elif isinstance(b, (int, float)) is False:
            raise TypeError("b must be an integer")
        return int(a) + int(b)
    except Exception:
        raise
