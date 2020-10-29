#!/usr/bin/env python
#
# description: Verifying an Alien Dictionary
# difficulty: Easy
# leetcode_num: 953
# leetcode_url: https://leetcode.com/problems/verifying-an-alien-dictionary/
#
# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of
# the alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.
#
# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#
# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


def AreWordsSorted(words, alphabet):
    if not len(words) or len(words) == 0:
        return True

    order = {}
    for i, char in enumerate(alphabet):
        order[char] = i

    for i in range(len(words)-1):
        currentWord = words[i]
        nextWord = words[i+1]

        if not inSortedOrder(currentWord, nextWord, order):
            return False

    return True


def inSortedOrder(word1, word2, order):
    size = min(len(word1), len(word2))

    for i in range(size):
        if order[word1[i]] > order[word2[i]]:
            return False

    return len(word1) <= len(word2)