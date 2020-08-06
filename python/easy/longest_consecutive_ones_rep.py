#!/usr/bin/env python
#
# description: Max Consecutive Ones
# difficulty: Easy
# leetcode_num: 485
# leetcode_url: https://leetcode.com/problems/max-consecutive-ones/
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s.
#
# Example 1:
#
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
# Example 2:
#
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#
# Note:
#
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 


def LongestConsecutiveOnes(nums, rep):
    if not nums:
        return 0

    start = 0
    end = 0

    while end < len(nums):
        if nums[end] == 0:
            rep -= 1

        if rep < 0:
            if nums[start] == 0:
                rep += 1
            start += 1

        end += 1

    return end - start