#!/usr/bin/python3
"""checking for inheritance"""


def inherits_from(obj, a_class):
    """checking where we inherited from"""

    if isinstance(obj, a_class):
        return type(obj) != a_class

    return False
