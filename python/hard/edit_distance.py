#!/usr/bin/env python
#
# description: Edit Distance
# difficulty: Hard
# leetcode_num: 72
# leetcode_url: https://leetcode.com/problems/edit-distance/
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


def getMinEditDistance(source, dest, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if source[m-1] == dest[n-1]:
        return getMinEditDistance(source, dest, m-1, n-1) # No edits

    return 1 + min(
        getMinEditDistance(source, dest, m, n-1),   # Character addition
        getMinEditDistance(source, dest, m-1, n),   # Charater removal
        getMinEditDistance(source, dest, m-1, n-1), # Charater replacement
    )


# Recursive Solution
def MinEditDistanceRecursive(source, dest):
    return getMinEditDistance(source, dest, len(source), len(dest))


# Solution using dynamic programming
def MinEditDistance(source, dest):
    m = len(source)
    n = len(dest)

    dist = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dist[i][j] = j
            elif j == 0:
                dist[i][j] = i
            elif source[i-1] == dest[j-1]:
                dist[i][j] = dist[i-1][j-1] # No edits
            else:
                dist[i][j] = 1 + min(
                    dist[i][j-1],   # Character addition
                    dist[i-1][j],   # Charater removal
                    dist[i-1][j-1]  # Charater replacement
                )

    return dist[m][n]


if __name__ == '__main__':
    test_cases = [
        (('horse', 'ros'), 3),
        (('intention', 'execution'), 5)
    ]

    for args, res in test_cases:
        assert MinEditDistanceRecursive(args[0], args[1]) == res, 'Test Failed'
        assert MinEditDistance(args[0], args[1]) == res, 'Test Failed'
