#!/usr/bin/env python
#
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5],
# its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2],
# its length is 1. 
# Note: Length of the array will not exceed 10,000.


def LongestSequenceLen(numbers):
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