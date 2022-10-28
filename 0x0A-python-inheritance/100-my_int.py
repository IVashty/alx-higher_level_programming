#!/usr/bin/python3
"""
Module 100-my_int
It inherits from int
"""


class MyInt(int):
    def __eq__(self, other):
        """
        equal is not equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        not  equal is equal
        """
        return super().__eq__(other)
