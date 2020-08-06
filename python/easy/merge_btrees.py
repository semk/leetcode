#!/usr/bin/env python
#
# description: Merge Two Binary Trees
# difficulty: Easy
# leetcode_num: 617
# leetcode_url: https://leetcode.com/problems/merge-two-binary-trees/
#
# Given two binary trees and imagine that when you put one of them to cover
# the other, some nodes of the two trees are overlapped while the others are
# not.
#
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7


def MergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2

    if tree2 is None:
        return tree1

    tree1.data += tree2.data

    tree1.left = MergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = MergeBinaryTrees(tree1.right, tree2.right)
    return tree1
