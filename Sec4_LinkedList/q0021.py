#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1 >= l2:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
            else:
                cur.next = l1
                l1 = l1.next
                cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next

