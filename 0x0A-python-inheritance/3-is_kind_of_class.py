#!/usr/bin/python3
"""this function checks if instance or type"""


def is_kind_of_class(obj, a_class):
    """checking if is instance of class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
