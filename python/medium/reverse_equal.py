#!/usr/bin/env python


def AreTheyEqual(array1, array2):
    if len(array1) != len(array2):
        return False

    left = 0
    right = len(array2) - 1
    leftBoundaryFound = False
    rightBoundaryFound = False

    mid = len(array1) // 2
    while left <= mid:
        if array1[left] != array2[left]:
            leftBoundaryFound = True
            right -= 1
        if array1[right] != array2[right]:
            rightBoundaryFound = True
            left += 1

        if leftBoundaryFound and rightBoundaryFound:
            break
    else:
        return reverseCompare(array1, array2, left, right)

    return True


def reverseCompare(array1, array2, left, right):
    mid = (left + right) // 2
    while left <= mid:
        if array1[left] != array2[right]:
            return False
        left += 1
        right -= 1
    return True