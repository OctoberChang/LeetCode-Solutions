#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0: return ""
        if n == 1: return s

        best_l, best_r = 0, 0
        for i in range(n):
            len_1 = self.expandStr(s, i, i)
            len_2 = self.expandStr(s, i, i+1)
            len_i = max(len_1, len_2)
            if len_i > (best_r - best_l):
                best_l = i - (len_i - 1)//2
                best_r = i + len_i // 2

        return s[best_l:best_r+1]

    def expandStr(self, s, l, r):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1



m = Solution()
s = 'babad'
print m.longestPalindrome(s)
