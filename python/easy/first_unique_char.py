#!/usr/bin/env python
#
# description: First Unique Character in a String
# difficulty: Easy
# leetcode_num: 387
# leetcode_url: https://leetcode.com/problems/first-unique-character-in-a-string/
#
# Given a string s, return the first non-repeating character in it and return
# its index. If it does not exist, return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
# Input: s = "aabb"
# Output: -1
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.


# Uses array
def FirstUniqueChar(text):
    char_ctr = [0] * 26

    for c in text:
        idx = ord(c) - ord('a')
        char_ctr[idx] += 1

    for i, c in enumerate(list(text)):
        idx = ord(c) - ord('a')
        if char_ctr[idx] == 1:
            return i

    return -1


# Uses dictionary
def FirstUniqueCharDict(text):
    char_ctr = {}

    for c in text:
        char_ctr.setdefault(c, 0)
        char_ctr[c] += 1

    for i, c in enumerate(list(text)):
        if char_ctr[c] == 1:
            return i

    return -1


if __name__ == '__main__':
    test_cases = [
        ('leetcode', 0),
        ('loveleetcode', 2),
        ('aabb', -1)
    ]

    for text, res in test_cases:
        assert FirstUniqueChar(text) == res, 'Test Failed'
        assert FirstUniqueCharDict(text) == res, 'Test Failed'
