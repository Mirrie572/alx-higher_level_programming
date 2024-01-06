#!/usr/bin/python3
"""This module defines a function that adds two integers.

The module includes a function named `add_integer` that takes two parameters,
`a` and `b`, and returns their sum. The default value for `b` is set to 98.

Usage:
    from 0-add_integer import add_integer

Example:
    result = add_integer(3, 5)
    print(result)  # Output: 8
"""


def add_integer(a, b=98):
    """Adds two integers or floats and returns their sum.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
