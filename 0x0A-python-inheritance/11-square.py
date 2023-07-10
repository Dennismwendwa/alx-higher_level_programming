#!/usr/bin/python3
"""this is class geometry"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """this is class square"""

    def __init__(self, size):
        """this are the atrributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    """This method returns the area"""
    def area(self):
        return super().area()

    """This method returns string reprecentation of square"""
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
