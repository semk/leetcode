#!/usr/bin/env python
#
# description: Climbing Stairs
# difficulty: Easy
# leetcode_num: 70
# leetcode_url: https://leetcode.com/problems/climbing-stairs/
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
# 1 <= n <= 45


def NumWaysToClimbStairs(stairs):
    prev, cur = 0, 1
    for _ in range(stairs):
        prev, cur = cur, prev + cur

    return cur


if __name__ == '__main__':
    assert NumWaysToClimbStairs(0) == 1, "Test Failed"
    assert NumWaysToClimbStairs(1) == 1, "Test Failed"
    assert NumWaysToClimbStairs(2) == 2, "Test Failed"
    assert NumWaysToClimbStairs(3) == 3, "Test Failed"
    assert NumWaysToClimbStairs(4) == 5, "Test Failed"