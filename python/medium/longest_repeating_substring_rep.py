#!/usr/bin/env python
#
# description: Longest Repeating Character Replacement
# difficulty: Medium
# leetcode_num: 424
# leetcode_url: https://leetcode.com/problems/longest-repeating-character-replacement/
#
# Given a string s that consists of only uppercase English letters, you can
# perform at most k operations on that string.
#
# In one operation, you can choose any character of the string and change it
# to any other uppercase English character.
#
# Find the length of the longest sub-string containing all repeating letters
# you can get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


def LongestRepeatingSubstringWithReplacement(s, rep):
    if not s:
        return 0

    start = 0
    end = 0
    maxLen = 0
    currentLen = 0
    remainingRep = rep

    while end < len(s):
        if s[end] == s[start]:
            currentLen += 1
            maxLen = max(maxLen, currentLen)
            end += 1
        elif remainingRep > 0:
            while remainingRep > 0:
                if s[end] != s[start]:
                    remainingRep -= 1
                    currentLen += 1
                    maxLen = max(maxLen, currentLen)
                    end += 1
                else:
                    break
        else:
            end -= (currentLen-rep)
            start = end
            currentLen = 0
            remainingRep = rep

    return maxLen
