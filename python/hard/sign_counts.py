#!/usr/bin/env python


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


def FindSignatureCountsUF(bookHolders):
    numStudents = len(bookHolders)
    uf = UF(numStudents)
    signCounts = []
    for i in range(numStudents):
        uf.union(i, bookHolders[i] - 1)

    for i in range(numStudents):
        signCounts.append(uf.size(i))

    return signCounts
