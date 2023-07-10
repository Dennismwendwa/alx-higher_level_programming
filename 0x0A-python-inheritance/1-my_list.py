#!/usr/bin/python3
"""
This is class Mylist with its attributes and methods
"""


class MyList(list):
    """ this are the attributes"""

    def print_sorted(self):
        """this method prints sorted list"""
        lists = sorted(self)
        print(lists)
