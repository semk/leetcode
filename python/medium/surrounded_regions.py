#!/usr/bin/env python
#
# description: Surrounded Regions
# difficulty: Medium
# leetcode_num: 130
# leetcode_url: https://leetcode.com/problems/surrounded-regions/
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be: 
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.


def SurroundedRegions(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        if grid[i][0] == 'O':
            markBorder(grid, i, 0)
        if grid[i][n-1] == 'O':
            markBorder(grid, i, n-1)

    for j in range(n):
        if grid[0][j] == 'O':
            markBorder(grid, 0, j)
        if grid[m-1][j] == 'O':
            markBorder(grid, m-1, j)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                grid[i][j] = 'X'
            elif grid[i][j] == '*':
                grid[i][j] = 'O'

    return grid


def markBorder(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return

    if grid[i][j] == 'O':
        grid[i][j] = '*'

    if i > 0 and grid[i-1][j] == 'O':
        markBorder(grid, i-1, j)
    if i < len(grid) -1 and grid[i+1][j]:
        markBorder(grid, i+1, j)
    if j > 0 and grid[i][j+1] == 'O':
        markBorder(grid, i, j+1)
    if j < len(grid[0]) - 1 and grid[i][j+1] == 'O':
        markBorder(grid, i, j-1)


if __name__ == '__main__':
    test_cases = [
        ([
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
        ],
        [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X'],
        ])
    ]

    for grid, res in test_cases:
        assert SurroundedRegions(grid) == res, 'Test Failed'
