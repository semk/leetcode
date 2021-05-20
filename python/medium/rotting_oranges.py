#!/usr/bin/env python
#
# description: Rotting Oranges
# difficulty: Medium
# leetcode_num: 994
# leetcode_url: https://leetcode.com/problems/rotting-oranges/
#
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
# Example 1:
# Input: grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4
#
# Example 2:
# Input: grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1
# Explanation: The orange in the bottom left corner(row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
# Example 3:
# Input: grid = [[0, 2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the
# answer is just 0.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


from collections import deque
import math


class RottenOrange:

    def __init__(self, pos, elapsed):
        self.pos = pos
        self.elapsed = elapsed


# Uses BFS to simulate the rotting oranges
def MinTimeToRotFreshOranges(basket):
    if len(basket) == 0:
        return 0

    rows = len(basket)
    cols = len(basket[0])
    rotten = deque()

    for i in range(rows):
        for j in range(cols):
            if basket[i][j] == 2:
                r = RottenOrange((i, j), 0)
                rotten.append(r)

    elapsed = 0
    while len(rotten) != 0:
        current = rotten.popleft()
        cur_i, cur_j = current.pos
        elapsed = max(elapsed, current.elapsed)

        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        for di, dj in directions:
            next_i, next_j = cur_i + di, cur_j + dj
            if next_i >= 0 and next_i < rows and next_j >= 0 and next_j < cols and basket[next_i][next_j] == 1:
                basket[next_i][next_j] = 2
                r = RottenOrange((next_i, next_j), current.elapsed + 1)
                rotten.append(r)

    for i in range(rows):
        for j in range(cols):
            if basket[i][j] == 1:
                return -1

    return elapsed


if __name__ == '__main__':
    test_cases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0)
    ]

    for inp, res in test_cases:
        assert MinTimeToRotFreshOranges(inp) == res, 'Test Failed'
