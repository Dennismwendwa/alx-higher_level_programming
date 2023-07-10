#!/usr/bin/python3
"""this is class geomentry"""


class BaseGeometry:
    """this are the attributes"""

    def area(self):
        raise Exception("area() is not implemented")

    """this method validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is class base rectangle"""
    def __init__(self, width, height):
        """this are the attributes of the class"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    """this method returns area"""
    def area(self):
        return self.__width * self.__height

    """this method return str reprecentation of the rectangle class"""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """this is class square"""

    def __init__(self, size):
        """this are the attributes"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    """This method returns the area"""
    def area(self):
        return super().area()
