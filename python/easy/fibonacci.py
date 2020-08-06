#!/usr/bin/env python


def Fibonacci(n):
    cur, nxt = 0, 1
    for _ in range(n):
        cur, nxt = nxt, cur + nxt

    return cur