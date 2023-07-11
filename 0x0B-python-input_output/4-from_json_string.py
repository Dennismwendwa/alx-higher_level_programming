#!/usr/bin/python3
"""This function loads json string"""


def from_json_string(my_str):
    """
    This function return python object reprecentation of string
    Argmumets:
        my_str: string
    """
    import json
    return json.loads(my_str)
