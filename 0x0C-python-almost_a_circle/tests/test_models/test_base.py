"""Unittest for Base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_base_id(self):
        self.assertEqual(Base(10).id, 10)

    def test_no_id(self):
        self.assertEqual(Base().id, 1)

    def test_neg_id(self):
        self.assertEqual(Base(-5).id, -5)
