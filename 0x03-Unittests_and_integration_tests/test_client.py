#!/usr/bin/env python3
"""
Module to test Client module
"""

import unittest
from unittest import mock
from unittest.mock import patch
import client
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Class to test Githubclient class"""

    @parameterized.expand([
        ("google", ),
        ("abc")
    ])
    @patch('client.get_json', return_value=1)
    def test_org(self, org, return_value):
        """Test the org method"""
        test_client = client.GithubOrgClient(org)
        self.assertEqual(test_client.org, 1)
        client.get_json.assert_called_once_with(client.GithubOrgClient.
                                                ORG_URL.format(org=org))
