#!/usr/bin/python3
"""checking if is instance of class"""


def is_same_class(obj, a_class):
    """
    this method checkis if is instance
    this are the attributes:
        obj: object of class
        a_class: instance
    """
        
    if type(obj) == a_class:
        return True
    else:
        return False
