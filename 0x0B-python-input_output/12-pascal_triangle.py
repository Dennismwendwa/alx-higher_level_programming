#!/usr/bin/python3
"""this is he pescal triangle"""


def pascal_triangle(n):
    """this function returns list"""
    if n <= 0:
        return []

    triangle = [[1]]
    for k in range(1, n):
        rw = [1]
        prev_rw = triangle[k - 1]
        for m in range(1, k):
            rw.append(prev_rw[m - 1] + prev_rw[m])
        rw.append(1)
        triangle.append(rw)

    return triangle
