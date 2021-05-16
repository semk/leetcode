#!/usr/bin/env python
#
# description: Toeplitz Matrix
# difficulty: Easy
# leetcode_num: 766
# leetcode_url: https://leetcode.com/problems/toeplitz-matrix/
#
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
# Example 1:
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:
#
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99


def IsToeplitzMatrix(matrix):
    if len(matrix) == 0:
        return True

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            # Simply check if previous top left element is the same or not
            if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] != matrix[i][j]:
                return False

    return True


if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True),
        ([[1, 2], [2, 2]], False)
    ]

    for matrix, res in test_cases:
        assert IsToeplitzMatrix(matrix) == res, 'Test Failed'
