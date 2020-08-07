#!/usr/bin/env python
#
# description: Count Contiguous Subarrays
# difficulty: Hard
# leetcode_num: 
# leetcode_url: https://leetcode.com/discuss/interview-question/579606/count-contiguous-subarrays
#
# You are given an array a of N integers. For each index i, you are required
# to determine the number of contiguous subarrays that fulfills the following
# conditions:
# The value at index i must be the maximum element in the contiguous subarrays,
#   and
# These contiguous subarrays must either start from or end with i.
#
# Output
# An array where each index i contains an integer denoting the maximum number
# of contiguous subarrays of a[i]
# Example:
# a = [3, 4, 1, 6, 2]
# output = [1, 3, 1, 5, 1]
#
# Explanation:
# For index 0 - [3] is the only contiguous subarray that starts (or ends) with
# 3, and the maximum value in this subarray is 3.
# For index 1 - [4], [3, 4], [4, 1]
# For index 2 -[1]
# For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
# For index 4 - [2]
# So, the answer for the above input is [1, 3, 1, 5, 1]


def FindContiguousSubArrays(array):
    arrayLen = len(array)
    subArrayCounts = [arrayLen] * arrayLen
    stack = []

    for index, item in enumerate(array):
        while stack and item >= array[stack[-1]]:
            subArrayCounts[stack.pop()] -= arrayLen - index
        stack.append(index)

    stack.clear()

    for index, item in reversed(list(enumerate(array))):
        while stack and array[index] >= array[stack[-1]]:
            subArrayCounts[stack.pop()] -= index + 1
        stack.append(index)

    return subArrayCounts