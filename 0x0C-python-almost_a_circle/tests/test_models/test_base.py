#!/usr/bin/python3
"""this are the test for base class"""


import os
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(100)
        base4 = Base(500)
        base5 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 100)
        self.assertEqual(base4.id, 500)
        self.assertEqual(base5.id, 3)

    def test_to_json_string(self):
        
        list_d = [{"id": 1}, {"id": 100}, {"id": 2}]
        json_string = Base.to_json_string(list_d)

        outcome = '[{"id": 1}, {"id": 100}, {"id": 2}]'
        self.assertEqual(json_string, outcome)


    def test_save_to_file(self):

        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(1, 2)
        sq1 = Square(5)
        sq2 = Square(6)

        Rectangle.save_to_file([rect1, rect2])
        Square.save_to_file([sq1, sq2])

        assert os.path.exists("Rectangle.json")
        assert os.path.exists("Square.json")

    def test_create(self):
        sset = {"id": 2}
        objects = Base(**sset)

        self.assertEqual(objects.id, 2)
