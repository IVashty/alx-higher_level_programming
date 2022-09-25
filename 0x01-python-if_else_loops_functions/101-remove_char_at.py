#!/usr/bin/python3
def remove_char_at(str, n):
    chr = 0
    new_str = ""
    for character in str:
        if chr != n:
            new_str += character
        chr += 1
    return new_str
