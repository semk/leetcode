#!/usr/bin/env python
#
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


def MultiplyMatrices(matrix_a, matrix_b):
    if not matrix_a or not matrix_b:
        return []

    a_rows = len(matrix_a)
    a_cols = len(matrix_a[0])
    b_rows = len(matrix_b)
    b_cols = len(matrix_b[0])
    if a_cols != b_rows:
        return []

    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(b_rows):
                product[i][j] += (matrix_a[i][k] * matrix_b[k][j])

    return product