#!/usr/bin/python3
"""
Module 1-my_list
It creates a clas inheriting from the list class.
"""


class MyList(list):
    """
    Mylist inherits from object list.
    """

    def print_sorted(self):
        """
        it prints an assorted list in ascending mode

        """
        print(sorted(self))
