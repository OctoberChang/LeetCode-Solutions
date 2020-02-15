#!/usr/bin/env python
# encoding: utf-8

import heapq

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # base subroutine
    def mergeTwoLists(l1, l2):
        curr = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists):
        # dummy case
        if not lists:
            return None

        left, right = 0, len(lists) - 1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = self.mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

    # Time:  O(nlogk)
    # Space: O(logk)
    # Divide and Conquer solution.
    def mergeKListsV2(self, lists):

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]

            l = mergeKListsHelper(lists, begin, (begin+end)/2)
            r = mergeKListsHelper(lists, (begin+end)/2 + 1, end)
            return self.mergeTwoLists(l, r)

        # call
        return mergeKListsHelper(lists, 0, len(lists) - 1)

    # Time: O(nklogk)
    # Space: O(k)
    # Heap solution
    def mergeKListsV3(self, lists):
        curr = dummy = ListNode(-1)

        heap = []
        for idx, sorted_list in enumerate(lists):
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, idx))

        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            node = lists[idx].next
            lists[idx] = node
            if node:
                heapq.heappush(heap, (node.val, idx))

        return dummy.next()
