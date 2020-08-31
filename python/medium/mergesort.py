#!/usr/bin/env python
#
# description: Sort an Array - Meregesort
# difficulty: Medium
# leetcode_num: 912
# leetcode_url: https://leetcode.com/problems/sort-an-array/


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    arr_left = [0] * (n1)
    arr_right = [0] * (n2)

    for i in range(0, n1):
        arr_left[i] = arr[left + i]

    for j in range(0, n2):
        arr_right[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if arr_left[i] <= arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr_left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr_right[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)


def MergeSort(arr):
    mergeSort(arr, 0, len(arr)-1)
    return arr


if __name__ == '__main__':
    test_cases = [
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10])
    ]

    for arr, res in test_cases:
        assert MergeSort(arr) == res, 'Test Failed'
