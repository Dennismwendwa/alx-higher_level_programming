#!/usr/bin/python3
"""This function searches and adds string"""


def append_after(filename="", search_string="", new_string=""):
    """This function searches and adds string
    Arguments:
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
        file.truncate()
