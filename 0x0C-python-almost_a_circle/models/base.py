"""
Creating a base class that with be te  foundation of our project
"""


class Base:
    """
    Declare a base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        A condition of where,if id is not None then we assign a instance of an
        attribute id(assuming it will be an integer) with an argument value
        else
        increment __nb_objects and assign new value to the public instance
        attribute id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def update(self, *args):
        a = ["id", "x", "y", "width", "height"]
        for i in range(len(args)):
            if i > len(a) - 1:
                break
            setattr(self, a[i], args[i])

    def update2(self, *args, **kwargs):
        b = ["id", "width", "height", "x", "y"]
        for j in range(len(args)):
            if j > len(b) - 1:
                break
            setattr(self, b[j], args[j])
        for key, value in kwargs.items():
            print("{} is {}".format(key, value))
