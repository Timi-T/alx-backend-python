#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in a list
of floats and return a float value
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function to sum all values of a list"""
    return sum(input_list)
