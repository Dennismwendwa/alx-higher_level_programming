#!/usr/bin/python3
"""
This is class rectangle with its attributes and methods
"""


from models.base import Base


class Rectangle(Base):
    """this is class rectangle attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the contructor of this class
        Attributes:
            __width: width
            __height: height
            __x: x
            __y: y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This method returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """this method returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this method sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This method returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """this method sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This method returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """this method sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this method reurns area"""
        return self.__width * self.__height

    def display(self):
        """this method prints rectangle using #"""
        for k in range(self.y):
            print()  # offset for y-coordinate
        for _ in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")  # offset for x-coordinate
            print("#" * self.__width)

    def __str__(self):
        """this method prints rectangle repricentation (__str__)"""
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
                )

    def update(self, *args, **kwargs):
        """this method uses *args to assign attributes"""
        if args:
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
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """this method returns dictionary representation of rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
