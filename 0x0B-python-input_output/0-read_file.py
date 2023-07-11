#!/usr/bin/python3
"""This is a function that reads files"""


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
