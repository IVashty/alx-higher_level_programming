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

        def my_get(self):
            return (self.width, self.height, self.x, self.y)

        def my_set(self, w, h, xx, yy):
            self.__width = w
            self.height = h
            self.__x = ex
            self.__y = wy

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
