#!/usr/bin/python3
"""This is class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the contractor of this class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """this method returns string reprecentation of square"""
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    """This method returns size"""
    @property
    def size(self):
        return self.width

    """This method sets size"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
