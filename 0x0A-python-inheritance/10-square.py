#!/usr/bin/python3
"""this is class geomentry"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """this is class square"""

    def __init__(self, size):
        """this are the attributes"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """This method returns the area"""
        return self.__size * self.__size

    """this is str method"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
