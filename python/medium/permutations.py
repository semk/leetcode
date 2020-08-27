#!/usr/bin/env python
#
# description: Permutations
# difficulty: Medium
# leetcode_num: 46
# leetcode_url: https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def genPermutations(nums, perms, current, used):
    if len(nums) == len(current):
        perms.append(current[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue

        current.append(nums[i])
        used[i] = True
        genPermutations(nums, perms, current, used)
        current.pop()
        used[i] = False


def GeneratePermutations(nums):
    perms = []
    used = [False] * len(nums)
    genPermutations(nums, perms, [], used)
    return perms


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ])
    ]

    for inp, res in test_cases:
        assert GeneratePermutations(inp) == res, 'Test Failed'
