#!/usr/bin/python3
"""
Module Rectangle
Inherit from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        My Initialiser
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def my_get(self):
            return (self.__width, self.__height, self.__x, self.__y)

        @my_get.setter
        def my_set(self, value):
            self.validate_integer("width", value, False)
            self.__width = value
            self.validate_integer("height", value, False)
            self.__height = value
            self.validate_integer("x", value)
            self.__x = value
            self.validate_integer("y", value)
            self.__y = value

        def validate_integer(self, name, value, eq=True):
            """
            My validator for checking values(if may be ts an in)
            """
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if eq and value < 0:
                raise TypeError("{} must be >= 0".format(name))
            elif not eq and value <= 0:
                raise ValueError("{} must be > 0".format(name))

        def area(self) -> int:
            """
            Finding the area of the rectangle
            """
            return self.width * self.height

        def __str__(self) -> str:
            """
            String representation
            """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
            )

        def check_typeofvalue(self, name: str, value: object, greater_equal=False):
            """
            type and value validation
            """
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if not greater_equal:
                if value <= 0:
                    raise ValueError("{} must be > 0".format(name))
                else:
                    if value < 0:
                        raise ValueError("{} must be >= 0".format(name))
