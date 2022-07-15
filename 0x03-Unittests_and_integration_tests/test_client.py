#!/usr/bin/env python3
"""
Module to test Client module
"""

import unittest
from unittest import mock
import client
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Class to test Githubclient class"""

    @parameterized.expand([
        ("google", ),
        ("abc")
    ])
    def test_org(self, org):
        """Test the org method"""
        with mock.patch('client.get_json', return_value=org) as mock_method:
            test_client = client.GithubOrgClient(org)
            self.assertEqual(test_client.org, org)
            mock_method.assert_called_once_with(client.GithubOrgClient.
                                                ORG_URL.format(org=org))
