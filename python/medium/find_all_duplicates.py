#!/usr/bin/env python
#
# description: Find All Duplicates in an Array
# difficulty: Medium
# leetcode_num: 442
# leetcode_url: https://leetcode.com/problems/find-all-duplicates-in-an-array/
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]


def FindDuplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] >= 0:
            nums[idx] = -nums[idx]
        else:
            duplicates.append(-nums[idx])

    return duplicates


if __name__== '__main__':
    assert FindDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [3, 2], 'Test Failed'
