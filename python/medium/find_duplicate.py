#!/usr/bin/env python
#
# description: Find the Duplicate Number
# difficulty: Medium
# leetcode_num: 287
# leetcode_url: https://leetcode.com/problems/find-the-duplicate-number/
#
# Given an array nums containing n + 1 integers where each integer is between
# 1 and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.


def FindDuplicate(nums):
    if len(nums) < 2:
        return -1
    
    # Using Floyd's Hare-Tortoise algorithm
    slow_ptr = nums[0]
    fast_ptr = nums[0]
    
    slow_ptr = nums[slow_ptr]
    fast_ptr = nums[nums[fast_ptr]]

    while slow_ptr != fast_ptr:
        slow_ptr = nums[slow_ptr]
        fast_ptr = nums[nums[fast_ptr]]

    a_ptr = nums[0]
    b_ptr = slow_ptr

    while a_ptr != b_ptr:
        a_ptr = nums[a_ptr]
        b_ptr = nums[b_ptr]

    return a_ptr


if __name__== '__main__':
    assert FindDuplicate([1, 3, 4, 2, 2]) == 2, 'Test Failed'
    assert FindDuplicate([3, 1, 3, 4, 2]) == 3, 'Test Failed'
    assert FindDuplicate([1, 1, 4, 3, 1]) == 1, 'Test Failed'
    assert FindDuplicate([1, 1]) == 1, 'Test Failed'
    assert FindDuplicate([3]) == -1, 'Test Failed'
    assert FindDuplicate([]) == -1, 'Test Failed'
