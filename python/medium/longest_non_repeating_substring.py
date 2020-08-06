#!/usr/bin/env python
#
# description: Longest Substring Without Repeating Characters
# difficulty: Medium
# leetcode_num: 3
# leetcode_url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not
# a substring.


def LongestNonRepeatingSubstring(s):
    if not s:
        return 0

    start = 0
    end = 0
    maxLen = 0
    seen = set()

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            maxLen = max(maxLen, len(seen))
            end += 1
        else:
            seen.remove(s[start])
            start += 1

    return maxLen