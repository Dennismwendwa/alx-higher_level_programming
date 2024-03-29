#!/usr/bin/python3
"""
This is class square with its attributes and methods
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the contractor of this class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this method returns string reprecentation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """This method returns size"""
        return self.width

    @size.setter
    def size(self, value):
        """This method sets size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method sets attributes using argsa and kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This method return dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
