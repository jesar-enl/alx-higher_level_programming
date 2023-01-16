#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.sq = Square(10, 0, 0, 3)

    def tearDown(self):
        self.sq.size = 10
        self.sq.x = 0
        self.sq.y = 0
        self.sq.id = 3

    def test_init(self):
        self.assertEqual(self.sq.width, 10)
        self.assertEqual(self.sq.height, 10)
        self.assertEqual(self.sq.x, 0)
        self.assertEqual(self.sq.y, 0)
        self.assertEqual(self.sq.id, 3)

    def test_str(self):
        expected = "[Square] (3) 0/0 - 10"
        self.assertEqual(str(self.sq), expected)

    def test_size(self):
        self.sq.size = 12

        self.assertEqual(self.sq.width, 12)
        self.assertEqual(self.sq.height, 12)

        with self.assertRaises(TypeError):
            self.sq.size = "12"

        with self.assertRaises(ValueError):
            self.sq.size = -12

    def test_update(self):
        self.sq.update(12, 31, 1, 2)
        expected = "[Square] (12) 1/2 - 31"
        self.assertEqual(str(self.sq), expected)

        self.sq.update(x=2, y=1, id=13, size=31)
        expected = "[Square] (13) 2/1 - 31"
        self.assertEqual(str(self.sq), expected)

    def test_to_dictionary(self):
        sq_dict = self.sq.to_dictionary()
        expected = {'id': 3, 'size': 10, 'x': 0, 'y': 0}
        self.assertDictEqual(sq_dict, expected)
