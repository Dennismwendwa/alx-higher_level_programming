#!/usr/bin/python3
"""This function write into file"""


def write_file(filename="", text=""):
    """this function writes into file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        length = len(text)
        file.write(text)
        return length
