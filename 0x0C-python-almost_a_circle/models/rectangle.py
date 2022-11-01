#!/usr/bin/python3
"""This module defines the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """
    Class that builds a Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instance of the Rectangle

        Args:
            width: width for the instance of type Rectangle
            height: height for the instance of type Rectangle
            x: number of spaces before printing a rectangle
            y: number of spaces before each row of the rectangle
            id: id of the object
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function for property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for property width

        Args:
            value: value for property width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for property height

        Args:
            value: value for property height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function for property x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter function for property x

        Args:
            value: value for property x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function for property y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter function for property y

        Args:
            value: value for property y
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the an instance of type Rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of the object"""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Function that updates an instance assigning arguments"""

        argumeents = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, argumeents[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        olddict = self.__dict__.copy()
        newdict = {}
        for i in olddict:
            newkey = i.replace('_Rectangle__', "")
            newdict[newkey] = self.__dict__[i]
        return newdict

