#!/usr/bin/env python
#
# description: Binary Tree Maximum Path Sum
# difficulty: Hard
# leetcode_num: 124
# leetcode_url: https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some starting
# node to any node in the tree along the parent-child connections. The path
# must contain at least one node and does not need to go through the root.
#
# Example 1:
# Input: root = [1,2,3]
# Output: 6
#
# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42


import math


class Result:
    max_path_sum = -math.inf


def MaximumPathSum(root):
    res = Result()
    pathSum(root, res)
    # pathSum2(root, res)
    return res.max_path_sum


def pathSum(node, res):
    if not node:
        return 0

    left = pathSum(node.left, res)
    right = pathSum(node.right, res)

    max_sum_inpath = max(max(left, right) + node.value, node.value)
    max_sum = max(max_sum_inpath, left + right + node.value)
    res.max_path_sum = max(res.max_path_sum, max_sum)
    return max_sum_inpath


def pathSum2(node, res):
    if not node:
        return 0

    left = max(pathSum2(node.left, res), 0)
    right = max(pathSum2(node.right, res), 0)

    res.max_path_sum = max(res.max_path_sum, left + right + node.value)
    return max(left, right) + node.value


if __name__ == '__main__':
    class Node:
        left = None
        right = None
        value = None

    def build_tree(positions, pos):
        if pos < len(positions) and positions[pos][0]:
            n = Node()
            n.value = positions[pos][1]
            n.left = build_tree(positions, (pos*2) + 1)
            n.right = build_tree(positions, (pos*2) + 2)
            return n

    test_cases = [
        # [1,2,3]
        ([(True, 1), (True, 2), (True, 3)], 6),
        # [-10,9,20,null,null,15,7]
        ([(True, -10), (True, 9), (True, 20), (False, -1), (False, -1), (True, 15), (True, 7)], 42),
        # [-1,-2,-3]
        ([(True, -1), (True, -2), (True, -3)], -1),
        # [-2,-1,-3]
        ([(True, -2), (True, -1), (True, -3)], -1),
    ]

    for tc, res in test_cases:
        tree = build_tree(tc, 0)
        assert MaximumPathSum(tree) == res, 'Test Failed'