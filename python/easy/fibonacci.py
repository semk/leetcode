#!/usr/bin/env python
#
# description: Fibonacci Number
# difficulty: Easy
# leetcode_num: 509
# leetcode_url: https://leetcode.com/problems/fibonacci-number/
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
# Example 1:
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# Note:
# 0 ≤ N ≤ 30.


def Fibonacci(n):
    cur, nxt = 0, 1
    for _ in range(n):
        cur, nxt = nxt, cur + nxt

    return cur


if __name__ == '__main__':
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5)
    ]

    for inp, res in test_cases:
        assert Fibonacci(inp) == res, 'Test Failed'