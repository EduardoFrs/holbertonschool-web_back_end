#!/usr/bin/env python3
"""Unit test"""

import unittest, requests

from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


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

class TestGetJson(unittest.TestCase):
    """ Test JSON """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Mock HTTP calls"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)
            mock_request.assert_called_once_with(test_url)
