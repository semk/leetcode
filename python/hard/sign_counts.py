#!/usr/bin/env python
#
# description: Passing Yearbooks
# difficulty: Hard
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


class UF:

    def __init__(self, size):
        self.ids = list(range(size))
        self.sizes = [1] * size

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a == root_b:
            return
        if self.sizes[root_a] > self.sizes[root_b]:
            self.ids[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.ids[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]

    def root(self, idx):
        while self.ids[idx] != idx:
            self.ids[idx] = self.ids[self.ids[idx]]
            idx = self.ids[idx]

        return idx

    def size(self, idx):
        root = self.root(idx)
        return self.sizes[root]


# O(n log n) solution using UnionFind
def FindSignatureCountsUF(bookHolders):
    numStudents = len(bookHolders)
    uf = UF(numStudents)
    signCounts = []
    for i in range(numStudents):
        uf.union(i, bookHolders[i] - 1)

    for i in range(numStudents):
        signCounts.append(uf.size(i))

    return signCounts


# O(n^2) solution (brute-force)
def FindSignatureCountsBF(bookHolders):
    signCounts = [1] * len(bookHolders)
    for student in bookHolders:
        studentIndex = student - 1
        while bookHolders[studentIndex] != student:
            signCounts[studentIndex] += 1
            studentIndex = bookHolders[studentIndex] - 1

    return signCounts


# O(n) solution using set
def FindSignatureCounts(bookHolders):
    signCounts = [0] * len(bookHolders)
    rootIndices = [-1] * len(bookHolders)
    visitedStudents = set()
    
    for i, student in enumerate(bookHolders):
        if student in visitedStudents:
            continue

        visitedStudents.add(student)
        # This is the root of the new passing cycle. Count from 1
        signCounts[i] = 1

        studentIndex = student - 1
        while bookHolders[studentIndex] != student:
            # Update the count at root of the cycle
            signCounts[i] += 1
            # Refer to the root of the cycle
            rootIndices[studentIndex] = i
            studentIndex = bookHolders[studentIndex] - 1
            visitedStudents.add(bookHolders[studentIndex])

    for i in range(len(bookHolders)):
        if rootIndices[i] != -1:
            # Find count from the root of the cycle
            signCounts[i] = signCounts[rootIndices[i]]

    return signCounts


if __name__ == '__main__':
    test_cases = [
        ([3, 2, 4, 1], [3, 1, 3, 3]),
    ]

    for pos, res in test_cases:
        assert FindSignatureCountsUF(pos) == res, 'Test Failed'
        assert FindSignatureCountsBF(pos) == res, 'Test Failed'
        assert FindSignatureCounts(pos) == res, 'Test Failed'