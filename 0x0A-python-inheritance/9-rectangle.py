#!/usr/bin/python3
"""Module 9-rectangle.py.
it uses the inherit for a new Rectangle form TASK 8
"""


taRectangle = __import__("8-rectangle").Rectangle


class Rectangle(taRectangle):
    """
    Class Rectangle based in BaseGeometry and other rectangle
    """

    def __init__(self, width, height):
        """Constructor of Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This method return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This method return the representation of the Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
