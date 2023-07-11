#!/usr/bin/python3
"""This function appends into file"""


def append_write(filename="", text=""):
    """function that appends in file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        length = len(text)
        file.write(text)
        return length
