#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def buildHelper(left, right):
            if left > right:
                return None

            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = buildHelper(left, mid-1)
            root.right = buildHelper(mid+1, right)
            return root

        return buildHelper(0, len(nums)-1)


class Solution2:
    def findMid(self, head):
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next

        if prev:
            prev.next = None

        return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None

        mid = self.findMid(head)
        root = TreeNode(mid.val)
        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
