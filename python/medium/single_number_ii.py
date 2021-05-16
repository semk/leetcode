#!/usr/bin/env python
#
# description: Single Number II
# difficulty: Medium
# leetcode_num: 137
# leetcode_url: https://leetcode.com/problems/single-number-ii/
#
# Given an integer array nums where every element appears three times 
# except for one, which appears exactly once. Find the single element 
# and return it.
#
# You must implement a solution with a linear runtime complexity and 
# use only constant extra space.
#
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#
# Constraints:
# 1 <= nums.length <= 3 * 104
# -2^31 <= nums[i] <= 2^31 - 1
# Each element in nums appears exactly three times except for one element which appears once.


BIT_LEN = 32


def SingleNumber(nums):
    # Keeps the set bits count at bits_count[i]
    bits_count = [0] * BIT_LEN

    for num in nums:
        for i in range(BIT_LEN):
            # count the set bits at i
            if num & (1 << i):
                bits_count[i] += 1

    single = 0
    for i, count in enumerate(bits_count):
        # If the count is not divisible by 3, it's the odd bit at i.
        if count % 3:
            single += (1 << i)

    return single


if __name__ == '__main__':
    test_cases = [
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99)
    ]

    for nums, res in test_cases:
        assert SingleNumber(nums) == res, 'Test Failed'
