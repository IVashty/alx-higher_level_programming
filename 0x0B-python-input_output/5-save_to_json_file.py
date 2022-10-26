#!/usr/bin/python3
"""
Module save_to_json_file
It witesa an object to a text file using
"""


def save_to_json_file(my_obj, filename):
    """
    i need JSON module cause its an external source.
    Function that writes an object to a text file
    Arguments:
        my_obj - py obj that will be converted to JSON
        filename - name of file
    """
    from json import dumps

    with open(filename, "w", encoding="utf-8") as f:
        f.write(dumps(my_obj))
        f.close()
