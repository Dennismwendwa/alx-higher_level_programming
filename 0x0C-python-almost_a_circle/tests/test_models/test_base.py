#!/usr/bin/python3
"""this are the test for base class"""


from turtle import Turtle
from unittest.mock import patch, MagicMock, call
import csv
import os
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """this is test for base class"""
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

    """this is test for to_json_string method"""
    def test_to_json_string(self):

        list_d = [{"id": 1}, {"id": 100}, {"id": 2}]
        json_string = Base.to_json_string(list_d)

        outcome = '[{"id": 1}, {"id": 100}, {"id": 2}]'
        self.assertEqual(json_string, outcome)

    """this is test for save_to_file"""
    def test_save_to_file(self):

        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(1, 2)
        sq1 = Square(5)
        sq2 = Square(6)

        Rectangle.save_to_file([rect1, rect2])
        Square.save_to_file([sq1, sq2])

        assert os.path.exists("Rectangle.json")
        assert os.path.exists("Square.json")

    """this is test for create method"""
    def test_create(self):
        sset = {"id": 2}
        objects = Base(**sset)

        self.assertEqual(objects.id, 2)

    """this test for load_from_file"""
    def test_load_from_file(self):
        filename = "Rectangle.json"

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write('[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
                       ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')

        instances = Rectangle.load_from_file()

        self.assertEqual(len(instances), 2)

        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 7)
        self.assertEqual(instances[0].x, 2)
        self.assertEqual(instances[0].y, 8)

        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[1].width, 2)
        self.assertEqual(instances[1].height, 4)
        self.assertEqual(instances[1].x, 0)
        self.assertEqual(instances[1].y, 0)

        os.remove(filename)

    """this is test for load from csv"""
    def test_load_from_file_csv(self):
        filename = "Square.csv"

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("1,7,0,0\n2,9,3,3")

        instances = Square.load_from_file_csv()

        self.assertEqual(len(instances), 2)

        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].size, 7)
        self.assertEqual(instances[0].x, 0)
        self.assertEqual(instances[0].y, 0)

        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[1].size, 9)
        self.assertEqual(instances[1].x, 3)
        self.assertEqual(instances[1].y, 3)

        os.remove(filename)

    """This is test for save to csv"""
    def test_save_to_file_csv(self):
        r1 = Rectangle(11, 12, 13, 14)
        r2 = Rectangle(20, 21, 22, 23)
        s1 = Square(33, 34, 35)

        Rectangle.save_to_file_csv([r1, r2])
        Square.save_to_file_csv([s1])

        with open("Rectangle.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0], ["10", "11", "12", "13", "14"])
            self.assertEqual(rows[1], ["11", "20", "21", "22", "23"])

        with open("Square.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0], ["12", "33", "34", "35"])
