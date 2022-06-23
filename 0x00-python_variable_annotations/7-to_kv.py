#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in a string
and an int/float and return a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to make a tuple from arguments"""
    return (k, (v ** 2))
