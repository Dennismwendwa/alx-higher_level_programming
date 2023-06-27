#!/usr/bin/python3
"""
This is class square with its attributes
"""


class Square:

    """This are the attributes"""

    def __init__(self, size=0, position=(0, 0)):

        """
        Attributes of the class

        Atrribyutes:
            size: size
            position: position
        """

        self.size = size
        self.position = position

    """This method finds area of the square"""
    def area(self):
        return self.__size * self.__size

    """This method gets the size of square"""
    @property
    def size(self):
        return self.__size

    """This method sets the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """This method prints # for both sides of the square"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.size):
            print("#" * self.__size, end="")
            print()

    """This method returns position"""
    @property
    def position(self):
        return self.__position

    """This method sets the position"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
