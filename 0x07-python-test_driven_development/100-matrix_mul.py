#!/usr/bin/python3
"""
Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists,
                   if m_a or m_b is empty,
                   if one element of those list of \
                           lists is not an integer or float,
                   if m_a and m_b can't be multiplied.
        ValueError: If m_a or m_b is not a rectangle \
                (all rows should be of the same size).
    """
    if not m_a or not isinstance(m_a, list) or not \
            all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not m_b or not isinstance(m_b, list) or not \
            all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
