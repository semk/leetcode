#!/usr/bin/env python
#
# description: Passing Yearbooks
# difficulty: Medium
# leetcode_num: 
# leetcode_url: https://leetcode.com/discuss/interview-question/614096/facebook-interview-preparation-question-passing-yearbooks
#
# There are n students, numbered from 1 to n, each with their own yearbook.
# They would like to pass their yearbooks around and get them signed by other
# students. You're given a list of n integers arr[1..n], which is guaranteed
# to be a permutation of 1..n (in other words, it includes the integers from
# 1 to n exactly once each, in some order). The meaning of this list is
# described below.
# Initially, each student is holding their own yearbook. The students will then
# repeat the following two steps each minute: Each student i will first sign
# the yearbook that they're currently holding (which may either belong to
# themselves or to another student), and then they'll pass it to student
# arr[i]. It's possible that arr[i] = i for any given i, in which case student
# i will pass their yearbook back to themselves. Once a student has received
# their own yearbook back, they will hold on to it and no longer participate in
# the passing process.
# It's guaranteed that, for any possible valid input, each student will
# eventually receive their own yearbook back and will never end up holding more
# than one yearbook at a time.
# You must compute a list of n integers output, whose ith element is equal to
# the number of signatures that will be present in student i's yearbook once
# they receive it back.


def FindSignatureCounts(bookHolders):
    signCounts = [1] * len(bookHolders)
    for student in bookHolders:
        studentIndex = student - 1
        while bookHolders[studentIndex] != student:
            signCounts[studentIndex] += 1
            studentIndex = bookHolders[studentIndex] - 1

    return signCounts