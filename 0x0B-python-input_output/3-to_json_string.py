#!/usr/bin/python3
"""This function return json string"""


import json


def to_json_string(my_obj):
    """This function returns json strings
    Arguments:
        my_obj: Object
    """
    return json.dumps(my_obj)
