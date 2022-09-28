#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for int in a_dictionary:
        new_dictionary[int] = a_dictionary[int] * 2
    return new_dictionary
