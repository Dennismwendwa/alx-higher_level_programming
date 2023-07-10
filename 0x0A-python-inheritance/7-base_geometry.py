#!/usr/bin/python3
"""This is class geometry with methods and attributes"""


class BaseGeometry:
    """This are the attributes and methods"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validate value
        atrributes:
            name: name
            value: value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
