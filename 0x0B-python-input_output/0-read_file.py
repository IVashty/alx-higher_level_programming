#!/usr/bin/python3
"""
Module read_file
It reads a text file(utf-8) and prints it
to stdout.
"""


def read_file(filename=""):
    """
    Reads filename with utf-8 and Prints  as stdout
    args:
        filename:name of the file
    """
    with open(filename, encoding="utf-8") as f:
        readtext = f.read()
        print(readtext, end="")
