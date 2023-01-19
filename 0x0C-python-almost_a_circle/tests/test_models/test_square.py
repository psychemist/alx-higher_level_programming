"""Unittest for Square
"""
import unittest
from models.square import Square


class TestBaseClass(unittest.TestCase):
    def test_square_id(self):
        self.assertEqual(Square(6).id, 6)
        self.assertEqual(Square(3, 5, 7, 11).id, 11)

    def test_size(self):
        self.assertEqual(Square(8).size, 8)

    def test_coordinates(self):
        self.assertEqual(Square(10, 3, 2).x, 3)
        self.assertEqual(Square(10, 3, 2).y, 2)

    def test_square_area(self):
        self.assertEqual(Square(6).area(), 36)
        self.assertEqual(Square(7, ).area(), 49)

