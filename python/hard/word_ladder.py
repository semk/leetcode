#!/usr/bin/env python
#
# description: Word Ladder
# difficulty: Hard
# leetcode_num: 127
# leetcode_url: https://leetcode.com/problems/word-ladder/
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ...
# -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need
# to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return
# the number of words in the shortest transformation sequence from beginWord
# to endWord, or 0 if no such sequence exists.
#
# Example 1:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is
# "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
#
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.


from collections import deque


ALPHABET = [chr(i) for i in range(ord('a'), ord('z')+1)]


# Uses BFS to store the character transformatations
def WordLadderLength(begin_word, end_word, word_list):
    word_list = set(word_list)
    if end_word not in word_list:
        return 0

    level = 1
    q = deque()
    q.append(begin_word)

    while len(q) != 0:
        qsize = len(q)
        for i in range(qsize):
            word = list(q.popleft())

            for i in range(len(word)):
                original_char = word[i]

                for c in ALPHABET:
                    if c == word[i]:
                        continue

                    word[i] = c
                    new_word = ''.join(word)
                    if new_word == end_word:
                        return level + 1

                    if new_word in word_list:
                        q.append(new_word)
                        word_list.remove(new_word)

                word[i] = original_char
        level += 1

    return 0


if __name__ == '__main__':
    test_cases = [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    ]

    for inp, res in test_cases:
        assert WordLadderLength(inp[0], inp[1], inp[2]) == res, 'Test Failed'
