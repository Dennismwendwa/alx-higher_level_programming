#!/usr/bin/python3
"""this is class geometry and its subclass"""


class BaseGeometry:
    """atributes of this class"""

    def area(self):
        raise Exception("area() is not implemented")


    """this method validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """This is class rectangle"""
    def __init__(self, width, height):
        """
        This attributres of this
        attributes:
            width: rectangle width
            height: rectangle height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
