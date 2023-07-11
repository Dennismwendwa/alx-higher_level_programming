#!/usr/bin/python3
"""This is class student and its method"""


class Student:
    """this are the attributes of this class
    attributes:
        first_name: first_name
        last_name: last_name
        age: age
    """
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    """This method retrieves dict representation"""
    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            attrs = self.__dict__.keys()
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]

        student_dict = {}
        for attr in attrs:
            student_dict[attr] = getattr(self, attr)

        return student_dict
