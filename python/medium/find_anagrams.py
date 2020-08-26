#!/usr/bin/env python
#
# description: Find All Anagrams in a String
# difficulty: Medium
# leetcode_num: 438
# leetcode_url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
#
# Given a string s and a non-empty string p, find all the start indices of
# p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


def FindAnagrams(text, anagram):
    if not text:
        return []

    charCounts = [0] * 26
    for c in anagram:
        charCounts[ord(c) - ord('a')] += 1

    start = 0
    end = 0
    count = len(anagram)
    anagramStartIndices = []
    
    while end < len(text):
        if charCounts[ord(text[end]) - ord('a')] > 0:
            charCounts[ord(text[end]) - ord('a')] -= 1
            end += 1
            count -= 1

        if count == 0:
            anagramStartIndices.append(start)

        if end - start == len(anagram) and charCounts[ord(text[start]) - ord('a')] >= 0:
            charCounts[ord(text[start]) - ord('a')] += 1
            start += 1
            count += 1

    return anagramStartIndices
