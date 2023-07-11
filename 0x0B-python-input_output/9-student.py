#!/usr/bin/python3
"""This is class student with its method"""


class Student:
    """
    this is class student
    attributes:
        first_name: first_name
        last_name: last_name
        age: age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """This method retrieves dictionary re[resentation of student instance"""
    def to_json(self):
        student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return student_dict
