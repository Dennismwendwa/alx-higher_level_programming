#!/usr/bin/python3
"""
This is class Mylist with its attributes and methods
"""


class MyList(list):
    """ this are the attributes"""
    
    def __init__(self):
        """contractor of the class """

        super().__init__()

    """this method prints sorted list"""
    def print_sorted(self):
        lists = sorted(self)
        print(lists)
