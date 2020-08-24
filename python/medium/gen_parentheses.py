#!/usr/bin/env python
#
# description: Generate Parentheses
# difficulty: Medium
# leetcode_num: 22
# leetcode_url: https://leetcode.com/problems/generate-parentheses/
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def genParenthesis(total, result, num_open, num_close, pattern):
    if num_open == total and num_close == total:
        result.append(pattern)
        return
    
    if num_open < total:
        genParenthesis(total, result, num_open + 1, num_close, pattern + '(')
    if num_close < num_open:
        genParenthesis(total, result, num_open, num_close + 1, pattern + ')')


def GenerateParentheses(total):
    result = []
    genParenthesis(total, result, 0, 0, '')
    return result


if __name__ == '__main__':
    test_cases = [
        (3, ['((()))', '(()())', '(())()', '()(())', '()()()'])
    ]

    for total, res in test_cases:
        assert GenerateParentheses(total) == res, 'Test Failed'
