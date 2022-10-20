#!/usr/bin/python3
"""
Module add-integer
Adds two integer together

"""


def add_integer(a, b):
    """
    First check if the input is correct,
    then cast both into ints and return the sum of a and b.
    """
    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError("a must be an integer")
        if isinstance(b, (int, float)) is False:
            raise TypeError("b must be an integer")
        return int(a) + int(b)
    except Exception:
        raise
