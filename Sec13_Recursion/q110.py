#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def getH(root):
            if not root: return 0

            l_h, r_h = getH(root.left), getH(root.right)
            if l_h < 0 or r_h < 0 or abs(l_h - r_h) > 1:
                return -1

            return 1 + max(l_h, r_h)

        # call sub-routine
        return (getH(root) >= 0)
