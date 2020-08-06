#!/usr/bin/env python


def reverseCompare(array1, array2, left, right):
    mid = (left + right) // 2
    while left <= mid:
        if array1[left] != array2[right]:
            return False
        left += 1
        right -= 1
    return True


def FindSignatureCounts(bookHolders):
    signCounts = [1] * len(bookHolders)
    for student in bookHolders:
        studentIndex = student - 1
        while bookHolders[studentIndex] != student:
            signCounts[studentIndex] += 1
            studentIndex = bookHolders[studentIndex] - 1

    return signCounts