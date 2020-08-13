#!/usr/bin/env python
#
# description: Container With Most Water
# difficulty: Medium
# leetcode_num: 11
# leetcode_url: https://leetcode.com/problems/container-with-most-water/
#
# Given n non-negative integers a1, a2, ..., an , where each represents a
# point at coordinate (i, ai). n vertical lines are drawn such that the two
# endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
# together with x-axis forms a container, such that the container contains
# the most water.
#
# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can
# contain is 49.
#
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


def ContainerWithMostWater(heights):
    start = 0
    end = len(heights) - 1
    max_vol = 0

    while end > start:
        width = end - start
        if heights[start] > heights[end]:
            height = heights[end]
            end -= 1
        else:
            height = heights[start]
            start += 1

        max_vol = max(max_vol, height * width)

    return max_vol


if __name__ == '__main__':
    heights = [1,8,6,2,5,4,8,3,7]
    assert ContainerWithMostWater(heights) == 49, "Test Failed"
