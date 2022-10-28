#!/usr/bin/python3
"""Module 8-rectangle.
it creates a BaseGeometry class.
"""


class BaseGeometry:
    """Class with public instance methods."""

    def area(self):
        """Raises an Exception with the message
        that says 'area() is not implemented'.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value if its an integer."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectangle based in BaseGeometry
    """

    def __init__(self, width, height):
        """Constructor of Retangle"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
