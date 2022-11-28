#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list = []
    for key, key_value in a_dictionary.items():
        if key_value is value:
            list.append(key)
    for l in list:
        del a_dictionary[l]
    return a_dictionary
