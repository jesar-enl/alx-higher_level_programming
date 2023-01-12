#!/usr/bin/python3
"""Module to contain the test cases for the name function"""

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """We are testing 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jesse Kyambadde' work?"""
        formatted_name = get_formatted_name('jesse', 'kyambadde')
        self.assertEqual(formatted_name, 'Jesse Kyambadde')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
