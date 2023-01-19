"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_rect_id(self):
        self.assertEqual(Rectangle(2, 5, 0, 0, 10).id, 10)
        self.assertEqual(Rectangle(5, 10).id, 4)
        self.assertEqual(Rectangle(1, 2, 0, 0, -1).id, -1)

    def test_lengths(self):
        self.assertEqual(Rectangle(2, 3).width, 2)
        self.assertEqual(Rectangle(2, 3).height, 3)

    def test_coordinates(self):
        self.assertEqual(Rectangle(2, 1, 5, 5, 11).x, 5)
        self.assertEqual(Rectangle(2, 1, 5, 5, 11).y, 5)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, [], 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 4, -5)

    def test_area(self):
        self.assertEqual(Rectangle(9, 17).area(), 153)

