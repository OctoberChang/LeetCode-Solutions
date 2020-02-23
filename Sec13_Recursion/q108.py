#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def buildHelper(left, right):
            if left > right: return None

            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = buildHelper(left, mid-1)
            root.right = buildHelper(mid+1, right)
            return root

        return buildHelper(0, len(nums)-1)


