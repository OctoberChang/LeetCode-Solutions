#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None or t1.val != t2.val:
            return False
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

    def isSymmetric2(self, root):
        if root is None: return True

        stack = [root.left, root.right]
        while stack:
            p, q = stack.pop(), stack.pop()
            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stacj.append(q.left)

        return True

