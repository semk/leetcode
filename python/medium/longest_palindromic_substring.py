#!/usr/bin/env python
#
# Given a string s, find the longest palindromic substring in s. You may
# assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


def LongestPalindromicSubstring(s):
    if not s:
        return ""

    start = 0
    end = 0
    maxLen = 0
    for i in range(len(s)):
        start1, end1, len1 = expandAndCompare(s, i, i)
        start2, end2, len2 = expandAndCompare(s, i, i+1)
        maxLen = max(max(len1, len2), maxLen)
        if maxLen == len1:
            start, end = start1, end1
        elif maxLen == len2:
            start, end = start2, end2

    return s[start:end+1]


def expandAndCompare(s, start, end):
    if not s or start > end:
        return 0, 0, 0

    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1

    return start + 1, end - 1, end - start + 1