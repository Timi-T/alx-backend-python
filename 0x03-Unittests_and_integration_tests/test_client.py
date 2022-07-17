#!/usr/bin/env python3
"""
Module to test Client module
"""

import client
import fixtures
from parameterized import parameterized, parameterized_class
import unittest
from unittest import mock
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Class to test Githubclient class"""

    @parameterized.expand([
        ("google", ),
        ("abc", )
    ])
    @patch('client.get_json', return_value="ok")
    def test_org(self, org, mock_object):
        """Test the org method"""
        test_client = client.GithubOrgClient(org)
        self.assertEqual(test_client.org, mock_object.return_value)
        mock_object.assert_called_once_with(client.GithubOrgClient.
                                            ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """Test _public_repos_url method"""
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as mock_method:
            test_client = client.GithubOrgClient("ope")
            ret = {"repos_url": "Payload"}
            mock_method.return_value = ret
            self.assertEqual(test_client._public_repos_url, ret["repos_url"])

    @patch('client.get_json', return_value=[{"name": "PL1"},
           {"name": "PL2", "license": "ok"}, {"name": "PL3"}])
    def test_public_repos(self, payloads):
        """Test public_repos method"""
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=PropertyMock) as mock_method:
            test_client = client.GithubOrgClient("ope")
            self.assertEqual(test_client.public_repos(),
                             [repo['name'] for repo in payloads.return_value])
            mock_method.assert_called_once()
            payloads.assert_called_once()
            client.get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, license, key, expected):
        """Test has_license method"""
        test_client = client.GithubOrgClient("ope")
        self.assertEqual(test_client.has_license
                         (repo=license, license_key=key), expected)


@parameterized_class([
    {"org_payload": fixtures.TEST_PAYLOAD[0][0]},
    {"repos_payload": fixtures.TEST_PAYLOAD[0][1]},
    {"expected_repos": fixtures.TEST_PAYLOAD[0][2]},
    {"apache2_repos": fixtures.TEST_PAYLOAD[0][3]}
], )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class For integeration tests"""

    @classmethod
    def setUpClass(cls):
        """Setup method for class"""
        with patch('requests.get', return_value=fixtures.TEST_PAYLOAD) as m:
            cls.get_patcher = mock.patch('requests.get.json',
                                         side_effect=fixtures.TEST_PAYLOAD[0][1][0])
            cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Teardown method for class"""
        cls.get_patcher.stop()
