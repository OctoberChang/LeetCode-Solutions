#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = float('-inf')
        self.MPS(root)
        return self.ans

    def MPS(self, root):
        if not root: return float('-inf')
        l = max(0, self.MPS(root.left))
        r = max(0, self.MPS(root.right))
        self.ans = max(self.ans, l + r + root.val)
        return root.val + max(l, r)

