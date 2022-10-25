#!/usr/bin/python3

"""
Module write_file
It writes a string to a text file in utf-8
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text filename
    Arguments:
        filename - name of the file
        text- should be string to write in the file

    Returns: the number of characters written.
    """
    with open(filename, "w+") as f:
        return f.write(text)
