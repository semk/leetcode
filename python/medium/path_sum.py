#!/usr/bin/env python
#
# description: Path Sum II
# difficulty: Medium
# leetcode_num: 113
# leetcode_url: https://leetcode.com/problems/path-sum-ii/
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


def FindPathsRecursive(node, req_sum):
    paths = []
    findPaths(node, req_sum, paths, [node.value])
    return paths


def findPaths(node, req_sum, paths, current_path):
    if not node:
        return

    if not node.left and not node.right and sum(current_path) == req_sum:
        paths.append(current_path)

    if node.left:
        findPaths(node.left, req_sum, paths, current_path + [node.left.value])
    if node.right:
        findPaths(node.right, req_sum, paths, current_path + [node.right.value])


def FindPaths(root, req_sum):
    if not root:
        return []

    stack = [(root, [root.value])]
    paths = []
    while len(stack) > 0:
        node, path = stack.pop()
        if not node.left and not node.right and sum(path) == req_sum:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + [node.left.value]))
        if node.right:
            stack.append((node.right, path + [node.right.value]))

    return paths


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
        (([(True, 5), (True, 4), (True, 8), (True, 11), (False, -1), (True, 13), (True, 4), (True, 7),
           (True, 2), (False, -1), (False, -1), (False, -1), (False, -1), (True, 5), (True, 1)], 22), True)
    ]

    for tc, res in test_cases:
        t, num = tc
        tree = build_tree(t, 0)
        assert FindPaths(tree, num) == [[5, 8, 4, 5], [5, 4, 11, 2]], 'Test Failed'
        assert FindPathsRecursive(tree, num) == [[5, 4, 11, 2], [5, 8, 4, 5]], 'Test Failed'
