#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in a list
of floats or integers and return a float value
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to sum up values in a list"""
    return float(sum(mxd_lst))
