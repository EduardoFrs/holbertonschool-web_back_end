#!/usr/bin/env python3
"""Unit test"""

import unittest

from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Gitghub ORG Client """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """ Test organization
        """
        mock_get_json.return_value = {"login": input}
        test_class = GithubOrgClient(input)
        test_class.org
        self.assertEqual(result, {"login": input})
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{input}')