#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        self.ans = 0
        def dfs(node):
            if node is None: return 0
            l = dfs(node.left)
            if node.left:
                l += 1
            r = dfs(node.right)
            if node.right:
                r += 1
            self.ans = max(self.ans, l + r)
            return max(l, r)

        dfs(root)
        return self.ans




