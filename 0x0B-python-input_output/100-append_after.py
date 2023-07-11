#!/usr/bin/python3
"""This function searches and adds string"""


def append_after(filename="", search_string="", new_string=""):
    """This function searches and adds string
    Arguments:
    """
    add = []
    with open(filename, mode="r", encoding="utf-8") as file:


        for lin in file:
            add += [lin]
            if lin.find(search_string) != -1:
                add += [new_string]


        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("".join(add))
