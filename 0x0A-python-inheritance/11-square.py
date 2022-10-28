#!/usr/bin/python3
"""Module Square.
it uses the inherit for a new Rectangle form TASK 9
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    this square inherits from Square
    """

    def __init__(self, size):
        """Constructor of square"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        My string representation of the Square
        """
        return "[Square]{0:d}/{0:d}".format(self.__size, self.__size)
