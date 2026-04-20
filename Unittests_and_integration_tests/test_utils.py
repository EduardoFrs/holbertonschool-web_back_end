#!/usr/bin/env python3
"""Unit test"""


from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test methode"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), None),
        ({"a": 1}, ("a", "b"), None)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test methode"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path), expected