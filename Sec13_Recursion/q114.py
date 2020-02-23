#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def flattenHelper(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        # now the real one
        tail_l = self.flattenHelper(root.left)
        tail_r = self.flattenHelper(root.right)

        if tail_l:
            tail_l.right = root.right
            root.right = root.left
            root.left = None
        return tail_r if tail_r else tail_l


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenHelper(root)

