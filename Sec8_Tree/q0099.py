#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, firstTime = None, None, True
        prev = TreeNode(float("-inf"))

        # in-order Morris traversal algo
        while root:
            # left-tree exist, go left
            if root.left:
                node = root.left
                # find right-most child of root.left
                while node.right and node.right != root:
                    node = node.right

                if node.right is None:
                    node.right = root
                    root = root.left
                else:
                    # visit root
                    if prev.val > root.val and firstTime:
                        first = prev
                        firstTime = False
                    if prev.val > root.val and not firstTime:
                        second = root
                    prev = root

                    node.right = None
                    root = root.right
            # left-tree empty, visit right
            else:
                # visit root
                if prev.val > root.val and firstTime:
                    first = prev
                    firstTime = False
                if prev.val > root.val and not firstTime:
                    second = root
                prev = root
                root = root.right

        # end while
        if first and second:
            first.val, second.val = second.val, first.val

