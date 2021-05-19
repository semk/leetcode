#!/usr/bin/env python
#
# description: Merge k Sorted Lists
# difficulty: Hard
# leetcode_num: 23
# leetcode_url: https://leetcode.com/problems/merge-k-sorted-lists/
#
# You are given an array of k linked-lists lists, each linked-list is sorted
# in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []


from heapq import heappush, heappop


# n: total number of elements in all lists. k: total number of lists
# Time Complexity: O(n log k)
# Space Complexity: O(log k)
def MergeKSortedLists(lists):
    result = []
    heap = []

    # Push first item of each list to the min-heap
    for i, l in enumerate(lists):
        if len(l) > 0:
            # Store the element along with it's position
            heappush(heap, (l[0], (i, 0)))

    while len(heap) != 0:
        num, pos = heappop(heap)
        result.append(num)
        i, j = pos
        if j < len(lists[i])-1:
            heappush(heap, (lists[i][j+1], (i, j+1)))

    return result


if __name__ == '__main__':
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], [])
    ]

    for inp, res in test_cases:
        assert MergeKSortedLists(inp) == res, 'Test Failed'
