#!/usr/bin/python3
"""This function returns the available attributes and methods of obj."""


def lookup(obj):
    """function that returns list of the objects"""
    avil = dir(obj)
    return avil
