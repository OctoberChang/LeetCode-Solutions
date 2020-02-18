#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # i: start index of pre
        # j: start index of post
        # n: length
        def build(i, j, n):
            # do sth
            if n <= 0: return None

            root = TreeNode(pre[i])
            if n == 1: return root

            k = j
            while post[k] != pre[i+1]: k += 1
            l = k - j + 1

            root.left = build(i+1, j, l)
            root.right = build(i+l+1, k+1, n - l -1)
            return root

        return build(0, 0, len(pre))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # i: start index of pre
        # j: start index of post
        # n: length
        def build(i, j, n):
            # do sth
            if n <= 0: return None

            root = TreeNode(pre[i])
            if n == 1: return root

            k = index[pre[i+1]]
            l = k - j + 1
            root.left = build(i+1, j, l)
            root.right = build(i+l+1, k+1, n - l -1)
            return root

        index = {}
        for i in range(len(pre)):
            index[post[i]] = i
        return build(0, 0, len(pre))
