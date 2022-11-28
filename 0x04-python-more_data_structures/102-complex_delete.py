#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for number in list(a_dictionary.keys()):
        if a_dictionary is value:
            del a_dictionary[number]
    return a_dictionary
