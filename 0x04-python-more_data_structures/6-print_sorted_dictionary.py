#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for int in sorted(a_dictionary.keys()):
        print("{}: {}".format(int, a_dictionary[int]))
