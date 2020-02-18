#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):

        ans = []

        def inorderRecursive(node):
            if node is None:
                return

            inorderRecursive(node.left)
            ans.append(node.val)
            inorderRecursive(node.right)
            return

        inorderRecursive(root)
        return ans

	def inorderTraversalV2(self, root):
        if root is None: return []

        ans = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node is None:
                continue

            if type(cur_node) is not TreeNode:
                ans.append(cur_node)
                continue

            stack.append(cur_node.right)
            stack.append(cur_node.val)
            stack.append(cur_node.left)

        return ans

