#!/usr/bin/python3
"""This is class geometry and its subclass"""


class BaseGeometry:
    """class attributes"""

    def area(self):
        raise Exception("area() is not implemented")

    """This method validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this is class rectangle"""

    def __init__(self, width, height):
        """
        This are the attribtes of the class
        atrributes:
            width: width
            height: height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)

    """This method returns area"""
    def area(self):
        return self.__width * self.__height

    """this method return string representation of the rectangle class"""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
