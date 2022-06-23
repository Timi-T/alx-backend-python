#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in any data type
and returns either none or anydatatype
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """Function to return a value from a dictionary using its"""
    if key in dct:
        return dct[key]
    else:
        return default
