#!/usr/bin/python3
"""
Module MyList
it creates a class inheriting from the  class list.
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
