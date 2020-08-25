#!/usr/bin/env python
#
# description: Count of Smaller Numbers After Self
# difficulty: Hard
# leetcode_num: 315
# leetcode_url: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number
# of smaller elements to the right of nums[i].
#
# Example 1:
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
# Constraints:
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


class Node:

    def __init__(self, data):
        self.data = data
        self.smaller_count = 1
        self.left = None
        self.right = None


def CountSmaller(nums):
    if not nums:
        return []

    res = [0]

    root = Node(nums[-1])

    for num in reversed(nums[:-1]):
        node = Node(num)
        count = addToBST(root, node)
        res.append(count)

    res.reverse()
    return res


def addToBST(root, node):
    count = 0
    added = False

    while not added:
        if node.data <= root.data:
            root.smaller_count += 1
            if root.left:
                root = root.left
            else:
                root.left = node
                added = True
        else:
            count += root.smaller_count
            if root.right:
                root = root.right
            else:
                root.right = node
                added = True

    return count



if __name__ == '__main__':
    test_cases = [
        ([5, 2, 6, 1], [2, 1, 1, 0])
    ]

    for nums, res in test_cases:
        print(CountSmaller(nums))
        assert CountSmaller(nums) == res, 'Test Failed'
