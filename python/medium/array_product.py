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


def ArrayProduct(array):
    arrayLen = len(array)

    leftProduct = [1] * arrayLen
    rightProduct = [1] * arrayLen

    for index in range(arrayLen - 1):
        rightIndex = arrayLen - 1 - index
        leftProduct[index+1] = leftProduct[index] * array[index]
        rightProduct[rightIndex-1] = rightProduct[rightIndex] * \
            array[rightIndex]

    productArray = []
    for index in range(arrayLen):
        productArray.append(leftProduct[index] * rightProduct[index])

    return productArray