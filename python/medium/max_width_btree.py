#!/usr/bin/env python
#
# description: Maximum Width of Binary Tree
# difficulty: Medium
# leetcode_num: 662
# leetcode_url: https://leetcode.com/problems/maximum-width-of-binary-tree/
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of 32-bit signed integer.
#
# Example 1:
#
# Input:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
#
# Constraints:
# The given binary tree will have between 1 and 3000 nodes.


def MaxWidthBTree(root):
    leftmost = {}
    return getWidth(root, leftmost, 0, 0, 0)


def getWidth(node, leftmost, level, position, max_width):
    if not node:
        return max_width

    leftmost.setdefault(level, position)
    max_width = max(max_width, position - leftmost[level] + 1)
    max_width = getWidth(node.left, leftmost, level + 1,
                         (position*2) + 1, max_width)
    max_width = getWidth(node.right, leftmost, level + 1,
                         (position*2) + 2, max_width)
    return max_width


if __name__ == '__main__':
    class Node:
        left = None
        right = None

    def build_tree(positions, pos):
        if pos < len(positions) and positions[pos]:
            n = Node()
            n.left = build_tree(positions, (pos*2) + 1)
            n.right = build_tree(positions, (pos*2) + 2)
            return n

    test_cases = [
        ([1, 1, 1, 1, 1, 0, 1], 4),
        ([1, 1, 0, 1, 1], 2),
        ([1, 1, 1, 1], 2),
        ([1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], 8)
    ]

    for tc, res in test_cases:
        tree = build_tree(tc, 0)
        assert MaxWidthBTree(tree) == res, 'Test Failed'
