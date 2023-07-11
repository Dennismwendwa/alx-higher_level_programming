#!/usr/bin/python3
import json
"""function that creates object from json file"""


def load_from_json_file(filename):
    """this function reads json from file, convert to python object"""
    with open(filename, mode="r", encoding="utf-8") as file:
        json_d = file.read()
        python_obj = json.loads(json_d)
        return python_obj
