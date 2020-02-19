#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSame(self, s, t):
        if s is None and t is None: return True
        if s is not None and t is None: return False
        if s is None and t is not None: return False

        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is not None: return False
        if s is not None and t is None: return False
        if s is None and t is None: return True

        if self.isSame(s, t):
            return True

        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        else:
            return False

