#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        # split into half
        fast, slow, prev = head, head, None
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        l = self.sortList(head)
        r = self.sortList(slow)
        return self.mergeList(l, r)

    def mergeList(self, l, r):

        dummy = ListNode(-1)
        cur = dummy
        while l and r:
            if l.val < r.val:
                cur.next, cur, l = l, l, l.next
            else:
                cur.next, cur, r = r, r, r.next

        if l:
            cur.next = l
        if r:
            cur.next = r
        return dummy.next

