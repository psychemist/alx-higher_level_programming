#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.test = [] 

    def test_max_beginning(self):
        self.assertEqual(max_integer([100, 90, 80, 70, 60]), 100)

    def test_max_middle(self):
        self.assertEqual(max_integer([40, 50, 1000, 60, 70]), 1000)

    def test_max_end(self):
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)

    def test_neg_number(self):
        self.assertEqual(max_integer([1, 2, -1, 3, 2, 1]), 3)

    def test_only_negatives(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_one_elem(self):
        self.assertEqual(max_integer([15]), 15)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_string_lists(self):
        self.assertEqual(max_integer("6789"), '9')
        self.assertEqual(max_integer("abcxyz"), 'z')
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y', 'z']), 'z')

    def test_list_of_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_other_types(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})

if __name__ == '__main__':
    unittest.main()

#   run test with python -m unittest -v tests.6-max_integer_test.py
