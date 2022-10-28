#!/usr/bin/python3
"""Module Square.
it uses the inherit for a new Rectangle form TASK 9
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    this square inherits from Rectangle
    """

    def __init__(self, size):
        """Constructor of square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """This method return the area of the Square"""
        return self.__size**2
