#!/usr/bin/env python
#
# description: House Robber
# difficulty: Easy
# leetcode_num: 198
# leetcode_url: https://leetcode.com/problems/house-robber/
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping
# you from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent
# houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight
# without alerting the police.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: 
#     Rob house 1 (money = 1) and then rob house 3 (money = 3).
#     Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation:
#     Rob house 1 (money = 2), rob house 3 (money = 9) and 
#     rob house 5 (money = 1).
#     Total amount you can rob = 2 + 9 + 1 = 12.
#
# Constraints:
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400


def RobMaxMoney(houses):
    if not houses:
        return 0

    prevMax, curMax = 0, houses[0]
    for houseAmt in houses[1:]:
        prevMax, curMax = curMax, max(curMax, houseAmt + prevMax)

    return curMax


if __name__ == '__main__':
    test_cases = [
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12)
    ]

    for inp, res in test_cases:
        assert RobMaxMoney(inp) == res, 'Test Failed'
