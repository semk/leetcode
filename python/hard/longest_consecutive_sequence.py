#!/usr/bin/env python
#
# description: Longest Consecutive Sequence
# difficulty: Hard
# leetcode_num: 128
# leetcode_url: https://leetcode.com/problems/longest-consecutive-sequence/
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.


def LongestConsecutiveSequence(numbers):
    if not numbers:
        return 0
    
    uniqueNumbers = set()
    for num in numbers:
        uniqueNumbers.add(num)

    longestSeqLen = 1
    for currentNum in numbers:
        currentSeqLen = 1
        # Check if this number is the lowest in the sequence
        if currentNum-1 not in uniqueNumbers:
            # Now look only for increments
            while currentNum+1 in uniqueNumbers:
                currentSeqLen += 1
                currentNum += 1
            longestSeqLen = max(longestSeqLen, currentSeqLen)

    return longestSeqLen