#!/usr/bin/env python
#
# description: Add Two Numbers
# difficulty: Medium
# leetcode_num: 2
# leetcode_url: https://leetcode.com/problems/add-two-numbers/
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class LinkedList:

    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


def AddTwoNumbers(l1, l2):
    dummy = LinkedList(0)
    l3 = dummy
    carry = 0

    while l1 != None or l2 != None:
        l1_val = l1.val if l1 != None else 0
        l2_val = l2.val if l2 != None else 0

        current_sum = l1_val + l2_val + carry
        carry = current_sum // 10
        digit = current_sum % 10

        node = LinkedList(digit)
        l3.next = node

        l1 = l1.next if l1 != None else l1
        l2 = l2.next if l2 != None else l2
        l3 = l3.next

    if carry > 0:
        node = LinkedList(carry)
        l3.next = node
        l3 = l3.next

    return dummy.next


if __name__ == '__main__':

    def print_list(l):
        while l != None:
            print(l.val, end=' -> ')
            l = l.next
        print()

    def from_list(l):
        res = []
        while l != None:
            res.append(l.val)
            l = l.next

        return res

    def build_list(l):
        dummy = LinkedList(0)
        n = dummy
        for i in l:
            node = LinkedList(i)
            n.next = node
            n = n.next

        return dummy.next

    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([4, 7], [5, ], [9, 7]),
    ]

    for l1, l2, res in test_cases:
        l1 = build_list(l1)
        l2 = build_list(l2)
        assert from_list(AddTwoNumbers(l1, l2)) == res, 'Test Failed'
