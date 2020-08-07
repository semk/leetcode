#!/usr/bin/env python
#
# description: Check If Words Are Sorted Using Given Albhabet
# difficulty: Medium
# leetcode_num: 
# leetcode_url: 


def AreWordsSorted(words, alphabet):
    if not len(words) or len(words) == 0:
        return True

    ids = {}
    for i, char in enumerate(alphabet):
        ids[char] = i

    for i in range(len(words)-1):
        currentWord = words[i]
        nextWord = words[i+1]

        if not inSortedOrder(currentWord, nextWord, ids):
            return False

    return True


def inSortedOrder(word1, word2, ids):
    size = min(len(word1), len(word2))

    for i in range(size):
        if ids[word1[i]] > ids[word2[i]]:
            return False

    return len(word1) <= len(word2)