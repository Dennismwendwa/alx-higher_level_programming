#!/usr/bin/python3
"""This is the class Base"""


import json


class Base:
    """This is atrributes of class base
    Atrributes:
        __nb_objects: __nb_objects
        id: id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ the constructor of the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """this method returns JSON strings"""
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    """this method saves json string to file"""
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_string)
