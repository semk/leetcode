#!/usr/bin/env python
#
# description: Queens That Can Attack the King
# difficulty: Medium
# leetcode_num: 1222
# leetcode_url: https://leetcode.com/problems/queens-that-can-attack-the-king/
#
# On an 8x8 chessboard, there can be multiple Black Queens and one White King.
#
# Given an array of integer coordinates queens that represents the positions
# of the Black Queens, and a pair of coordinates king that represent the
# position of the White King, return the coordinates of all the queens
# (in any order) that can attack the King.
#
# Example 1:
#
# [['K', 'Q', '_', '_', 'Q', '_', '_', '_'],
#  ['Q', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', 'Q', '_', '_', '_'],
#  ['_', '_', '_', 'Q', '_', '_', '_', '_'],
#  ['Q', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_', '_', '_']]
#
# Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
# Output: [[0,1],[1,0],[3,3]]
# Explanation:  
# The queen at [0,1] can attack the king cause they're in the same row. 
# The queen at [1,0] can attack the king cause they're in the same column. 
# The queen at [3,3] can attack the king cause they're in the same diagnal. 
# The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].
# The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].
# The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.


def GetAttackingQueensCoordinates(queens, king):
    queenAtIndex = [[False for _ in range(8)]  for _ in range(8)]
    for x, y in queens:
        queenAtIndex[x][y] = True
    
    attackingQueuens = []
    directions = (-1, 0, 1)
    for dx in directions:
        for dy in directions:
            if dx == 0 and dy == 0:
                continue
           
            x, y = king
            while (x + dx < 8 and x + dx > 0 and y + dy < 8 and y + dy > 0):
                x, y = x + dx, y + dy
                if queenAtIndex[x][y]:
                    attackingQueuens.append((x, y))
                    break

    return attackingQueuens