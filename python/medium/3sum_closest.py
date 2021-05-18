#!/usr/bin/env python
#
# description: 3Sum Closest
# difficulty: Medium
# leetcode_num: 16
# leetcode_url: https://leetcode.com/problems/3sum-closest/
#
# Given an array nums of n integers and an integer target, find three
# integers in nums such that the sum is closest to target. Return the
# sum of the three integers. You may assume that each input would have
# exactly one solution.
#
# Example 1:
#
# Input: nums = [-1, 2, 1, -4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1=2).
#
# Constraints:
#
# 3 <= nums.length <= 10 ^ 3
# -10 ^ 3 <= nums[i] <= 10 ^ 3
# -10 ^ 4 <= target <= 10 ^ 4


import math


# O(n^2) solution involving sorting
def ThreeSumClosest(nums, target):
    total = len(nums)
    closest_sum = nums[0] + nums[1] + nums[total-1]

    nums.sort()

    for i in range(total-2):
        a_ptr = i + 1
        b_ptr = total - 1
        current_sum = nums[i] + nums[a_ptr] + nums[b_ptr]

        while a_ptr < b_ptr:
            if current_sum > target:
                b_ptr -= 1
            else:
                a_ptr += 1

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

    return closest_sum


if __name__ == '__main__':
    test_cases = [
        (([-1, 2, 1, -4], 1), 2)
    ]

    for inp, res in test_cases:
        arr, target = inp
        assert ThreeSumClosest(arr, target) == res, 'Test Failed'
