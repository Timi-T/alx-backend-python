#!/usr/bin/env python3
"""
Parameterize a unit test
"""


from typing import Mapping, Sequence, Union
from parameterized import parameterized
import unittest
from unittest import mock
import utils
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for utils.access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, output) -> Union[Mapping, int]:
        """Test to access a nested map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """Test nested access for exceptions"""
        self.assertRaises(KeyError, utils.access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests Class for utils.get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, test_payload) -> Mapping:
        """Test for correct results"""
        class Payload():
            """Create a mock reponse having a .json method"""
            def __init__(self, obj):
                """Constructor method"""
                self.obj = obj

            def json(self):
                """Define a json method"""
                return self.obj

        with mock.patch('requests.get', return_value=Payload(test_payload))\
                as mock_method:
            self.assertEqual(utils.get_json(url), test_payload)
            mock_method.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Tests for a memoizing wrapper"""

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    TClass = TestClass
    def test_memoize(self):
        """Test a memoizing wrapper"""

        with mock.patch('test_utils.TestMemoize.TClass.a_method',
                        return_value=42) as mock_method:
            test = TestMemoize.TClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()
