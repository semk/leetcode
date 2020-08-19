#!/usr/bin/env python
#
# description: Partition Labels
# difficulty: Medium
# leetcode_num: 763
# leetcode_url: https://leetcode.com/problems/partition-labels/
#
# A string S of lowercase English letters is given. We want to partition this
# string into as many parts as possible so that each letter appears in at most
# one part, and return a list of integers representing the size of these parts.
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits S into less parts.
#
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.


def PartitionLabels(array):
    if not array:
        return []

    lastSeenAt = {}
    for i, c in enumerate(array):
        lastSeenAt[c] = i

    start = 0
    end = 0
    partitions = []

    for i, c in enumerate(array):
        end = max(end, lastSeenAt[c])
        if i == end:
            partitions.append(end-start+1)
            start = end + 1

    return partitions