#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def validPalindrome(self, s):
        n = len(s)
        if n == 1: return True

        l, r = 0, n-1
        while l < r:
            if s[l] != s[r]:
                ans_l = self.check(s, l+1, r)
                ans_r = self.check(s, l, r-1)
                return ans_l or ans_r
            else:
                l += 1
                r -= 1
        return True


    def check(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True



m = Solution()
s = "abca"
print m.validPalindrome(s)
