#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


        dummy = ListNode(-1)
        dummy.next = head

        first, second = dummy, dummy
        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


