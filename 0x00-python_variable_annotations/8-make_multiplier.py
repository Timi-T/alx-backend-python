#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in a float
and return a function that multiplies the float by a number
"""
from typing import Callable


def multiplier_callback(num: float) -> float:
    return num * num


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return (multiplier_callback)
