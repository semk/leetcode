#!/usr/bin/env python
#
# description: One Edit Distance
# difficulty: Medium
# leetcode_num: 640
# leetcode_url: https://www.lintcode.com/problem/one-edit-distance/description
#
# Given two strings S and T, determine if they are both one edit distance
# apart.
# One ediit distance means doing one of these operation:
#
# insert one character in any position of S
# delete one character in S
# change one character in S to other character
# Have you met this question in a real interview?  
# Example
# Example 1:
#
# Input: s = "aDb", t = "adb" 
# Output: true
# Example 2:
#
# Input: s = "ab", t = "ab" 
# Output: false
# Explanation:
# s=t ,so they aren't one edit distance apart


def OneEditApart(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    if len(s1) - len(s2) > 1:
        return False

    alreadyEdited = False
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] != s2[j]:
            if alreadyEdited:
                return False

            alreadyEdited = True
            if len(s1) < len(s2):
                i -= 1

        i += 1
        j += 1

    return alreadyEdited or len(s1) != len(s2)