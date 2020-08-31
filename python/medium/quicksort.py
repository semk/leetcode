#!/usr/bin/env python
#
# description: Sort an Array - Quicksort
# difficulty: Medium
# leetcode_num: 912
# leetcode_url: https://leetcode.com/problems/sort-an-array/
#
# Given an array of integers nums, sort the array in ascending order.
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Constraints:
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000


def partition(arr, left, right):
    i = left - 1
    pivot = right

    for j in range(left, right):
        if arr[j] <= arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1


def quickSort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)


def QuickSort(arr):
    if len(arr) == 1:
        return arr

    left, right = 0, len(arr) - 1
    quickSort(arr, left, right)
    return arr


if __name__ == '__main__':
    test_cases = [
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10])
    ]

    for arr, res in test_cases:
        assert QuickSort(arr) == res, 'Test Failed'
