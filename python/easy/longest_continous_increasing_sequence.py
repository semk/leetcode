#!/usr/bin/env python
#
# description: Longest Continuous Increasing Subsequence
# difficulty: Easy
# leetcode_num: 674
# leetcode_url: https://leetcode.com/problems/longest-continuous-increasing-subsequence
#
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5],
# its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2],
# its length is 1. 
# Note: Length of the array will not exceed 10,000.


def LongestContinuousIncreasingSequence(numbers):
    result = 0
    anchor = 0

    for i in range(len(numbers)):
        if i > 0 and numbers[i-1] >= numbers[i]:
            anchor = i
        result = max(result, i - anchor + 1)

    return result
