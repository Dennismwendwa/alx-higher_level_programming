#!/usr/bin/python3
"""
This is class Mylist with its attributes and methods
"""


class MyList(list):
    """ this are the attributes"""
    
    """contractor of the class """
    def __init__(self):
        super().__init__()

    """this method prints sorted list"""
    def print_sorted(self):
        lists = list(self)
        lists.sort()
        print(lists)
