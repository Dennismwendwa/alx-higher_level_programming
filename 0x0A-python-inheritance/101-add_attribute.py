#!/usr/bin/python3
"""function that adds objects to class"""


def add_attribute(objects, name, value):
    """adding object to class"""
    if not hasattr(objects, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(objects, name, value)
