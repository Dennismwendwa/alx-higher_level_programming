#!/usr/bin/python3
"""This is class geometry with methods and attributes"""


class BaseGeometry:
    """This are the attributes
    attributes:
        name: name
        value: value
    """

    """This method returns area"""
    def area(self):
        raise Exception("area() is not implemented")

    """This method validate value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
