#!/usr/bin/python3
"""
Module 1-Rectangle
It should define a rectangle
"""


class Rectangle:
    """
    class : Rectangle
    Has two internal properties and methods to change them
    """

    @property
    def __init__(self, width=0, height=0):
        """Constructor.
        Arguments:
            width: The width of rectangle.
            height: The height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Property for the width of the rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        '''

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property for the height of the rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
