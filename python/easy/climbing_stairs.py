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


def NumWaysToClimbStairs(total_stairs):
    prev, cur = 0, 1
    for _ in range(total_stairs):
        prev, cur = cur, prev + cur

    return cur


# choices: This list defines the number of steps that can be taken at a time
def NumWaysToClimbStairsX(total_stairs, choices):
    if total_stairs == 0:
        return 1

    nums = [1]
    for i in range(1, total_stairs + 1):
        total = 0
        for j in choices:
            if i - j >= 0:
                total += nums[i-j]
        nums.append(total)

    return nums[total_stairs]


if __name__ == '__main__':
    test_cases = [
        (0, 1), (1, 1), (2, 2), (3, 3), (4, 5)
    ]

    for total_stairs, res in test_cases:
        assert NumWaysToClimbStairs(total_stairs) == res, "Test Failed"

    test_cases = [
        (5, (1 ,2, 3), 13)
    ]
    
    for total_stairs, choices, res in test_cases:
        assert NumWaysToClimbStairsX(total_stairs, choices) == res, "Test Failed"