#!/usr/bin/python3
"""This is the class Base"""


class Base:
    """This is atrributes of class base
    Atrributes:
        __nb_objects: __nb_objects
        id: id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ the constructor of the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
