#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def simplifyPath(self, path):

        s = path.split('/')
        stack = []

        for c in s:
            if c:
                if c == '..':
                    stack = stack[:-1]
                elif c != '.':
                    stack.append(c)
        return '/' + '/'.join(stack)

m = Solution()
s = '/a/./b/../../c/'
print s, ' ||| ', m.simplifyPath(s)
s = '/a/../../b/../c//.//'
print s, ' ||| ', m.simplifyPath(s)
s = '/a//b////c/d//././/..'
print s, ' ||| ', m.simplifyPath(s)
