#!/usr/bin/env python3
"""
Module to annotate a function's parameters and return values
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
