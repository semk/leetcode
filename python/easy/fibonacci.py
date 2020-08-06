#!/usr/bin/env python
#
# description: Fibonacci
# difficulty: Easy
# leetcode_num: 
# leetcode_url: 


def Fibonacci(n):
    cur, nxt = 0, 1
    for _ in range(n):
        cur, nxt = nxt, cur + nxt

    return cur