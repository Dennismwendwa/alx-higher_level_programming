#!/usr/bin/python3

"""This function returns the available attributes and methods of obj."""
def lookup(obj):
    avil = list(dir(obj))
    return avil
