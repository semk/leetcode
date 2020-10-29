#!/usr/bin/env python
#
# description: Median of Two Sorted Arrays
# difficulty: Hard
# leetcode_num: 4
# leetcode_url: https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000


import math


def MedianOfSortedArrays(nums_1, nums_2):
    if len(nums_1) > len(nums_2):
        nums_1, nums_2 = nums_2, nums_1

    lo = 0
    hi = len(nums_1)
    combinedLen = len(nums_1) + len(nums_2)

    while lo <= hi:
        partX = (lo + hi) // 2
        partY = ((combinedLen + 1) // 2) - partX

        leftX = getMax(nums_1, partX)
        rightX = getMin(nums_1, partX)

        leftY = getMax(nums_2, partY)
        rightY = getMin(nums_2, partY)

        if leftX <= rightY and leftY <= rightX:
            if combinedLen % 2 == 0:
                return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
            else:
                return max(leftX, leftY)

        if leftX > rightY:
            hi = partX - 1
        else:
            lo = partX + 1


def getMax(nums, index):
    if index == 0:
        return -math.inf
    else:
        return nums[index-1]


def getMin(nums, index):
    if index == len(nums):
        return math.inf
    else:
        return nums[index]


if __name__ == '__main__':
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]

    for n1, n2, res in test_cases:
        assert MedianOfSortedArrays(n1, n2) == res, 'Test Failed'
