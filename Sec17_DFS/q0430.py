#!/usr/bin/env python
# encoding: utf-8

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None: return head

        dummy = Node(-1, None, head, None)
        self.flattenHelper(dummy, head)
        dummy.next.prev = None
        return dummy.next

    def flattenHelper(self, prev, curr):
        if curr == None: return prev

        prev.next, curr.prev = curr, prev
        temp = curr.next
        tail = self.flattenHelper(curr, curr.child)
        curr.child = None
        return self.flattenHelper(tail, temp)


class SolutionDFS:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head

        dummy = Node(0, None, head, None)
        prev = dummy

        stack = [head]
        while stack:
            curr = stack.pop()

            curr.prev, prev.next = prev, curr

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr

        dummy.next.prev = None
        return dummy.next
