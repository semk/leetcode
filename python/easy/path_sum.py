#!/usr/bin/env python
#
# description: Path Sum
# difficulty: Easy
# leetcode_num: 112
# leetcode_url: https://leetcode.com/problems/path-sum/
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


def HasPathSumRecursive(root, req_sum):
    if not root:
        return False

    return hasPathSum(root, req_sum, root.value)


def hasPathSum(node, req_sum, current_sum):
    if not node.left and not node.right and current_sum == req_sum:
        return True

    hasSum = False
    if node.left:
        hasSum = hasSum or hasPathSum(
            node.left, req_sum, current_sum + node.left.value)
    if node.right:
        hasSum = hasSum or hasPathSum(
            node.right, req_sum, current_sum + node.right.value)

    return hasSum


def HasPathSum(root, req_sum):
    if not root:
        return False

    stack = [(root, root.value)]
    while len(stack) > 0:
        node, current_sum = stack.pop()
        if not node.left and not node.right and current_sum == req_sum:
            return True
        if node.left:
            stack.append((node.left, current_sum + node.left.value))
        if node.right:
            stack.append((node.right, current_sum + node.right.value))

    return False


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
        (([(True, 5), (True, 4), (True, 8), (True, 11), (False, -1), (True, 13), (True, 4),
           (True, 7), (True, 2), (False, -1), (False, -1), (False, -1), (True, 1)], 22), True)
    ]

    for tc, res in test_cases:
        t, num = tc
        tree = build_tree(t, 0)
        assert HasPathSum(tree, num), 'Test Failed'
