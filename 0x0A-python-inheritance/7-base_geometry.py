#!/usr/bin/python3
"""Module 7-base_geometry.
it creates a BaseGeometry class.
"""


class BaseGeometry:
    """Class with public instance methods."""

    def area(self):
        """
        Raises an Exception with the message
        that says 'area() is not implemented'.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value if it is an integer
        Arguments:
            name -is an str
            value is an int
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
