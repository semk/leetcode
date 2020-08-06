#!/usr/bin/env python
#
# description: Passing Yearbooks
# difficulty: Medium
# leetcode_num: 
# leetcode_url: 


def FindSignatureCounts(bookHolders):
    signCounts = [1] * len(bookHolders)
    for student in bookHolders:
        studentIndex = student - 1
        while bookHolders[studentIndex] != student:
            signCounts[studentIndex] += 1
            studentIndex = bookHolders[studentIndex] - 1

    return signCounts