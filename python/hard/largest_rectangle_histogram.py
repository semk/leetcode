#!/usr/bin/env python
#
# description: Largest Rectangle in Histogram
# difficulty: Hard
# leetcode_num: 84
# leetcode_url: https://leetcode.com/problems/largest-rectangle-in-histogram/
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# Example:
# Input: [2,1,5,6,2,3]
# Output: 10


def LargestRectangle(histogram):
    start = 0
    end = len(histogram) - 1
    max_vol = 0

    while end > start:
        width = end - start
        if histogram[start] > histogram[end]:
            height = histogram[end]
            end -= 1
        else:
            height = histogram[start]
            start += 1

        max_vol = max(max_vol, height * width)

    return max_vol


if __name__ == '__main__':
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([2, 1, 5, 6, 2, 3], 10)
    ]

    for inp, res in test_cases:
        assert LargestRectangle(inp) == res, 'Test Failed'
