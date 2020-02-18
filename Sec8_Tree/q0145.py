#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []

        ans, stack = [], [root]
        while stack:
            cur_node = stack.pop()
            if cur_node is None:
                continue
            if type(cur_node) is not TreeNode:
                ans.append(cur_node)
                continue

            stack.append(cur_node.val)
            stack.append(cur_node.right)
            stack.append(cur_node.left)

        return ans
