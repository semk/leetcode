#!/usr/bin/env python
#
# description: N-Queens
# difficulty: Hard
# leetcode_num: 51
# leetcode_url: https://leetcode.com/problems/n-queens/
#
# The n-queens puzzle is the problem of placing n queens on an n×n
# chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


import pprint


def PlaceNQueens(size):
    colPlacements = []
    solveNQueens(size, 0, colPlacements)

    # Generate the size*size board with queens placed.
    board = [['.' for _ in range(size)] for _ in range(size)]
    for row, col in zip(range(size), colPlacements):
        board[row][col] = 'Q'

    return board


def solveNQueens(size, row, colPlacements,):
    if row == size:
        return True
    else:
        for col in range(size):
            colPlacements.append(col)
            if isValid(colPlacements):
                if solveNQueens(size, row+1, colPlacements):
                    return True
            colPlacements.pop()

    return False


def isValid(colPlacements):
    rowId = len(colPlacements) - 1
    for i in range(rowId):
        diff = abs(colPlacements[i] - colPlacements[rowId])
        if diff == 0 or diff == rowId-i:
            return False

    return True


if __name__ == '__main__':
    pprint.pprint(PlaceNQueens(6))
