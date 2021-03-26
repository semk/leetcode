#!/usr/bin/env python
#
# description: Product of Array Except Self
# difficulty: Medium
# leetcode_num: 238
# leetcode_url: https://leetcode.com/problems/product-of-array-except-self/
#
# Given an array nums of n integers where n > 1,  return an array output
# such that output[i] is equal to the product of all the elements of nums
# except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix
# or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).


def ArrayProduct(nums):
    res = []
    prod_left = 1
    for num in nums:
        res.append(prod_left)
        prod_left = prod_left * num

    prod_right = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i] * prod_right
        prod_right *= nums[i]

    return res


if __name__== '__main__':
    assert ArrayProduct([1, 2, 3, 4]) == [24, 12, 8, 6], 'Test Failed'
    assert ArrayProduct([]) == [], 'Test Failed'
    assert ArrayProduct([2]) == [1], 'Test Failed'