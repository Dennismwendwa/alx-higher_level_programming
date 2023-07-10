#!/usr/bin/python3
"""this is class myint"""


class MyInt(int):
    """this are the attributes"""

    def __eq__(self, my_int):
        """this is magic method __eq__"""
        return int.__ne__(self, my_int)

    def __ne__(self, my_int):
        """This is the opposite"""
        return int.__ge__(self, my_int)
