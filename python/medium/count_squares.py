#!/usr/bin/env python
#
# description: Count Square Submatrices with All Ones
# difficulty: Medium
# leetcode_num: 1277
# leetcode_url: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
#
# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
#
# Example 1:
#
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:
#
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.


def CountSquares(grid):
    m, n = len(grid), len(grid[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if i == 0 or j == 0:
                    count += 1
                else:
                    grid[i][j] = min(grid[i-1][j-1],
                                     grid[i][j-1],
                                     grid[i-1][j]) + grid[i][j]
                    count += grid[i][j]

    return count


if __name__ == '__main__':
    test_cases = [
        ([
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ], 15),
        ([
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ], 7)
    ]

    for grid, count in test_cases:
        assert CountSquares(grid) == count, 'Test Failed'
