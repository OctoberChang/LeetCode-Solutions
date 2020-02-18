#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []

        cur, ans = root, []
        while cur:
            # left sub-tree of current node is empty,
            # so visit right sub-tree
            if cur.left is None:
                ans.append(cur.val)
                cur = cur.right

            # visit left-subtree
            else:
                # find rightmost node of the left child of current node
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                # left-subtree not visited, so setup back-link
                # and visit left
                if node.right is None:
                    ans.append(cur.val)
                    node.right = cur
                    cur = cur.left
                # left-subtree already visited, so go back
                else:
                    node.right = None
                    cur = cur.right
        # return ans
        return ans
