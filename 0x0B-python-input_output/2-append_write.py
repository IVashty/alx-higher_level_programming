#!/usr/bin/python3
"""
Module append_write
It appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    adds a string at the end of a text filename
    Arguments:
        filename-name of file name
        text -be appended
    Return: The number of characters to be added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
