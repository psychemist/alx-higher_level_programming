"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_rect_id(self):
        self.assertEqual(Rectangle(2, 5, 0, 0, 10).id, 10)

    def test_no_id(self):
        self.assertEqual(Rectangle(5, 10).id, 1)

    def test_neg_id(self):
        self.assertEqual(Rectangle(1, 2, 0, 0, -1).id, -1)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, [], 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 4, -5)

