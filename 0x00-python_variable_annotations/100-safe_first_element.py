#!/usr/bin/env python3
"""
Module to define a type annotated function which takes in any data type
and returns either none or anydatatype
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the input typecasted to a list"""
    if lst:
        return lst[0]
    else:
        return None
