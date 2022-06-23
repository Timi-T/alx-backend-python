#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in any data type
and returns either none or anydatatype
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T", str, bytes)
def safely_get_value(dct: Mapping, key: Any, default: None):
    """Function to return a value from a dictionary using its key"""
    if key in dct:
        return dct[key]
    else:
        return default
