#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in a float
and return a function that multiplies the float by a number
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_callback(num: float) -> float:
        return float(multiplier * num)
    return(multiplier_callback)
