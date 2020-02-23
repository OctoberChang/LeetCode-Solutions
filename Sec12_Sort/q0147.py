#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or self.isSorted(head):
            return head

        dummy = ListNode(-1)
        dummy.next = head
        curr, tail = head.next, head
        while curr:
            prev = dummy
            while prev.next.val < curr.val:
                prev = prev.next
            if prev == tail:
                curr, tail = curr.next, curr
            else:
                curr.next, prev.next, tail.next = prev.next, curr, curr.next
                curr = tail.next
        return dummy.next


    def isSorted(self, head):
        while head and head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True
