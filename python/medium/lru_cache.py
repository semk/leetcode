#!/usr/bin/env python
#
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least
# recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class Node:

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class CacheOrder:

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        head_next = self.head.next
        self.head.next = node
        node.next = head_next
        node.prev = self.head

    def remove(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev


class LRUCache:

    def __init__(self, cacpacity):
        self.cacpacity = cacpacity
        self.cache = {}
        self.order = CacheOrder()

    def put(self, key, value):
        node = self.cache.get(key)
        if node:
            self.order.remove(node)
            node.value = value
            self.order.add(node)
        else:
            node = Node(key, value)
            if len(self.cache) == self.cacpacity:
                self.cache.pop(key)
                self.order.remove(self.order.tail.prev)
            
            self.cache[key] = node
            self.order.add(node)

    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.order.remove(node)
            self.order.add(node)
            return node.value
        else:
            return -1