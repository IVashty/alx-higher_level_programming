#!/usr/bin/python3
"""This module defines the class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that builds a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instance of the Rectangle

        Args:
            size: size for the instance of type Square
            x: number of spaces before printing a Square
            y: number of spaces before each row of the Square
            id: id of the object
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter function for property size"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter function for property size

        Args:
            value: value for property size
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the object"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Function that updates an instance assigning arguments"""

        props = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, props[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        newdict = {}
        olddict = self.__dict__.copy()
        for i in olddict:
            newkey = i.replace("_Rectangle__", "")
            if newkey == "width" or newkey == "height":
                newkey = "size"
            newdict[newkey] = self.__dict__[i]
        return newdict
