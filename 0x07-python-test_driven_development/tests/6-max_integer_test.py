#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""testing the max_integer function"""
	
	def test_max_integer_positive(self):
		self.assertEqual(max_integer([2, 3, 4, 5, 6]), 6)
		self.assertEqual(max_integer([6, 7, 11, 8, 9, 10]), 11)
		self.assertEqual(max_integer([99, 134, 84, 55, 45]), 134)

	def test_max_negative(self):
		self.assertEqual(max_integer([0]), 0)
		self.assertEqual(max_integer([9, 7, 16]), 16)
		self.assertEqual(max_integer([-1, -2, 3, 4]), 4)
		self.assertEqual(max_integer([21.3, 42.7, 6.5, 0.54]), 42.7)
		self.assertEqual(max_integer([-2434, -4335, -6573, -1111]), -1111)
		self.assertEqual(max_integer([{2, 5}, {2}]), {2, 5})

	def test_float_integer(self):
		self.assertEqual(max_integer([-6.1, -23.2, -3.43, -1.1]), -1.1)
		self.assertEqual(max_integer([1.2, 12.0, 24.8, 20.5]), 24.8)
		self.assertEqual(max_integer([999, 0.001, 1000, 344.2, 568.9]), 1000)

	def test_string(self):
		self.assertEqual(max_integer(["d", "y", "r"]), 'y')

	def test_raises_error(self):
		with self.assertRaises(TypeError):
			max_integer([1, "two", "five"])
		with self.assertRaises(TypeError):
			max_integer({2, 4, 6})
		with self.assertRaises(KeyError):
			max_integer({"key": 4, "key2": 5})
		with self.assertRaises(TypeError):
			max_integer(4, 7)

	def test_doscs(self):
		docts_av = __import__("6-max_integer").max_integer.__doc__
		print(docts_av)
		self.assertTrue(len(docts_av) > 2 )
