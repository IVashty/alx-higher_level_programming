#!/usr/bin/python3
def islower(c):
    alphabet = ord(c)
    if alphabet <= 122 and alphabet >= 97:
        return True
    else:
        return False
