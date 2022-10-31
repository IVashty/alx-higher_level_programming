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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        def __str__(self) -> str:
            """
            String representation
            """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
            )
