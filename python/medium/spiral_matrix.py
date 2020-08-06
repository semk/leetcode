#!/usr/bin/env python
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


def GenerateSpiral(size):
    grid = [[0] * size for _ in range(size)]
    populateSpiral(grid, 0, 1)
    return grid


def GenerateSpiralRect(numRows, numCols):
    grid = [[0] * numCols for _ in range(numRows)]
    populateSpiral(grid, 0, 1)
    return grid


def populateSpiral(grid, layer, count):
    numRows, numCols = len(grid), len(grid[0])

    if layer >= numRows // 2 and layer >= numCols // 2:
        return

    left, right, top, bottom = layer, numCols - \
        1 - layer, layer, numRows - 1 - layer
    # Fill top
    for idx in range(left, right):
        grid[top][idx] = count
        count += 1

    for idx in range(top, bottom):
        grid[idx][right] = count
        count += 1

    for idx in range(right, left, -1):
        grid[bottom][idx] = count
        count += 1

    for idx in range(bottom, top, -1):
        grid[idx][left] = count
        count += 1

    populateSpiral(grid, layer + 1, count)