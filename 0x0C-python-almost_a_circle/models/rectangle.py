#!/usr/bin/python3
"""This is class rectangle"""


from models.base import Base


class Rectangle(Base):
    """this is class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """this is the contructor of this class
        Attributes:
            __width: width
            __height: height
            __x: x
            __y: y
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """This method returns width"""
    @property
    def width(self):
        return self.__width

    """This method sets width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """this method returns height"""
    @property
    def height(self):
        return self.__height

    """this method sets the height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """This method returns x"""
    @property
    def x(self):
        return self.__x

    """this method sets x"""
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """This method returns y"""
    @property
    def y(self):
        return self.__y

    """this method sets y"""
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """this method reurns area"""
    def area(self):
        return self.__width * self.__height

    """this method prints rectangle using #"""
    def display(self):
        for k in range(self.y):
            print() # offset for y-coordinate
        for _ in range(self.__height):
            for _ in range(self.x):
                print(" ", end="") # offset for x-coordinate
            print("#" * self.__width)

    """this method prints rectangle repricentation (__str__)"""
    def __str__(self):
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
                )

    """this method uses *args to assign attributes"""
    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
