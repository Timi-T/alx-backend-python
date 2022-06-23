#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in a float
argumnt and returns an integer
"""
import math


def floor(n: float) -> int:
    """Function to convert a float to an integer"""
    return math.floor(n)
