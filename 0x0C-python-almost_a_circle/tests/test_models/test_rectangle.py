#!/usr/bin/python3
"""This are the tests for rectangle class"""

from io import StringIO
from unittest.mock import patch, MagicMock
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    """test for iniialization of the class"""
    def test_init(self):
        rect = Rectangle(20, 30, 2, 3, 1)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    """test for width getter and setter"""
    def test_width_getter_setter(self):
        rect = Rectangle(30, 40)
        rect.width = 4

        self.assertEqual(rect.width, 4)
        with self.assertRaises(TypeError):
            rect.width = "width must be an integer"

        with self.assertRaises(ValueError):
            rect.width = -8

    """this test is for height getters and setters"""
    def test_height_getter_setter(self):
        rect = Rectangle(30, 40)
        rect.height = 50

        self.assertEqual(rect.height, 50)
        with self.assertRaises(TypeError):
            rect.height = "height must be an integer"
        with self.assertRaises(ValueError):
            rect.height = -3

    """this test is for "x" getter and "setter" """
    def test_x_getter_setter(self):
        rect = Rectangle(30, 40)
        rect.x = 6

        self.assertEqual(rect.x, 6)
        with self.assertRaises(TypeError):
            rect.x = "x must be an integer"

        with self.assertRaises(ValueError):
            rect.x = -3
    """this is test for "y" getters and setters"""
    def test_y_getter_setter(self):
        rect = Rectangle(30, 40)
        rect.y = 0

        self.assertEqual(rect.y, 0)
        with self.assertRaises(TypeError):
            rect.y = "y must be an integer"

        with self.assertRaises(ValueError):
            rect.y = -3

    """this is test for area method"""
    def test_area(self):
        rect = Rectangle(30, 40)
        self.assertEqual(rect.area(), 1200)

    """this is test for display method"""
    def test_display(self):
        rect = Rectangle(3, 4)
        expected = "###\n###\n###\n###\n"
        with unittest.mock.patch("sys.stdout", new=StringIO()) as o:
            rect.display()
            self.assertEqual(o.getvalue(), expected)

    """this is test for str method"""
    def test_str(self):
        rect = Rectangle(30, 40, 4, 5, 1)
        expect_str = "[Rectangle] (1) 4/5 - 30/40"
        self.assertEqual(str(rect), expect_str)


class TestRectangleDict(unittest.TestCase):
    """this is test for rectangle and setup"""

    def setUp(self):
        self.rect = Rectangle(40, 50, 60, 70, 7)

    """this is test for update with args"""
    def test_update_with_args(self):
        self.rect.update(1, 2, 3, 4, 5)

        self.assertEqual(self.rect.id, 1)
        self.assertEqual(self.rect.width, 2)
        self.assertEqual(self.rect.height, 3)
        self.assertEqual(self.rect.x, 4)
        self.assertEqual(self.rect.y, 5)

    """this is test for up date with kwargs"""
    def test_update_with_kwargs(self):
        self.rect.update(width=4, height=2, x=10, y=15)

        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 2)
        self.assertEqual(self.rect.x, 10)
        self.assertEqual(self.rect.y, 15)

    """this is test for to dictionary method"""
    def test_to_dictionary(self):
        expect_dict = {
                "id": 7,
                "width": 40,
                "height": 50,
                "x": 60,
                "y": 70
                }
        self.assertEqual(self.rect.to_dictionary(), expect_dict)
