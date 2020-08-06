#!/usr/bin/env python
#
# description: Invert Binary Tree
# difficulty: Easy
# leetcode_num: 226
# leetcode_url: https://leetcode.com/problems/invert-binary-tree/
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


def InvertBinaryTree(root):
    if root == None:
        return

    left = InvertBinaryTree(root.left)
    right = InvertBinaryTree(root.right)

    root.left = right
    root.right = left

    return root