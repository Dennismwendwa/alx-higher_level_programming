#!/usr/bin/python3
"""this are the tests for class square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """this are the methods for this tests"""

    def setUp(self):
        self.square = Square(10, 4, 5, 7)

    """this test is for str"""
    def test_string_representation(self):
        expect_st = "[Square] (7) 4/5 - 10"

        self.assertEqual(str(self.square), expect_st)

    """this test is for get_size"""
    def test_get_size(self):
        self.assertEqual(self.square.size, 10)

    """this test is for set size"""
    def test_set_size(self):
        self.square.size = 20
        self.assertEqual(self.square.width, 20)
        self.assertEqual(self.square.height, 20)

    """this is test for typeerror insize"""
    def test_size_typeerror(self):
        with self.assertRaises(TypeError):
            self.square.size = "size must be a number"

    """this is test for value error in size"""
    def test_size_value_error(self):
        with self.assertRaises(ValueError):
            self.square.size = -4

    """this is test for square area"""
    def test_area(self):
        expect = 100
        self.assertEqual(self.square.area(), expect)

    """this test is for update with args"""
    def test_update_with_args(self):
        self.square.update(30, 40, 50, 60)
        self.assertEqual(self.square.id, 30)
        self.assertEqual(self.square.size, 40)
        self.assertEqual(self.square.x, 50)
        self.assertEqual(self.square.y, 60)

    """this test is for update with kwargs"""
    def test_update_with_kwargs(self):
        self.square.update(size=70, x=30, y=60)
        self.assertEqual(self.square.size, 70)
        self.assertEqual(self.square.x, 30)
        self.assertEqual(self.square.y, 60)

    """this test is for to_dictionary"""
    def test_to_dictionary(self):
        expect_st = {
                "id": 7,
                "size": 10,
                "x": 4,
                "y": 5
                }

        self.assertEqual(self.square.to_dictionary(), expect_st)


if __name__ == "__main__":
    unittest.main()
