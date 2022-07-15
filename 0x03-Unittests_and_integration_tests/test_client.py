#!/usr/bin/env python3
"""
Module to test Client module
"""

import client
from parameterized import parameterized
import unittest
from unittest import mock
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Class to test Githubclient class"""

    @parameterized.expand([
        ("google", ),
        ("abc")
    ])
    @patch('client.get_json', return_value=1)
    def test_org(self, org, mock_object):
        """Test the org method"""
        test_client = client.GithubOrgClient(org)
        self.assertEqual(test_client.org, mock_object.return_value)
        client.get_json.assert_called_once_with(client.GithubOrgClient.
                                                ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """Test pubic repos method"""
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as mock_method:
            test_client = client.GithubOrgClient("ope")
            ret = {"repos_url": "Payload"}
            mock_method.return_value = ret
            self.assertEqual(test_client._public_repos_url, ret["repos_url"])
