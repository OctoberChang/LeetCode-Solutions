#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def isValid(self, s):
        if len(s) == 0: return True

        n = len(s)
        stack = []
        map_dict = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in map_dict.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                c_top = stack.pop()
                if map_dict[c_top] != c:
                    return False
            print(c, stack)

        return True if len(stack) == 0 else False


m = Solution()
s = '()[]{}'
print m.isValid(s)
