#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next

