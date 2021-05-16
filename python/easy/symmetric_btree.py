#!/usr/bin/env python
#
# description: Symmetric Tree
# difficulty: Easy
# leetcode_num: 101
# leetcode_url: https://leetcode.com/problems/symmetric-tree/
#
# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3


def IsSymmetric(root):
    return isMirror(root, root)


def isMirror(node1, node2):
    if node1 == None and node2 == None:
        return True

    if node1 == None or node2 == None:
        return False

    if node1.data != node2.data:
        return False

    return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
