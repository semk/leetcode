#!/usr/bin/env python
#
# description: Path Sum III
# difficulty: Medium
# leetcode_num: 437
# leetcode_url: https://leetcode.com/problems/path-sum-iii/
#
# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must
# go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11



def FindPaths(root, req_sum):
    lookup = {req_sum: 1}
    return findPaths(root, req_sum, 0, 0, lookup)


def findPaths(node, req_sum, current_sum, total, lookup):
    if not node:
        return total

    current_sum += node.value
    print(current_sum)
    total += lookup.get(current_sum, 0)
    if current_sum+req_sum in lookup:
        lookup[current_sum+req_sum] += 1
    else:
        lookup[current_sum+req_sum] = 1

    print(lookup)
    total = findPaths(node.left, req_sum, current_sum, total, lookup)
    total = findPaths(node.right, req_sum, current_sum, total, lookup)

    lookup[current_sum+req_sum] -= 1

    return total


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

    # [10,5,-3,3,2,null,11,3,-2,null,1]
    test_cases = [
        (([(True, 10), (True, 5), (True, -3), (True, 3), (True, 2), (False, -1), (True, 11), (True, 3),
           (True, -2), (False, -1), (True, 1)], 8), 3)
    ]

    for tc, res in test_cases:
        t, num = tc
        tree = build_tree(t, 0)
        assert FindPaths(tree, num) == res, 'Test Failed'
    