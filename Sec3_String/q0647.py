#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def countSubstrings(self, s):
        n = len(s)
        if n == 1:
            return 1

        ans = 0
        for t in range(n):
            # odd case
            cnt_1 = self.expandStr(s, t, t)
            cnt_2 = self.expandStr(s, t, t+1)
            ans += cnt_1 + cnt_2
        return ans


    def expandStr(self, s, l, r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1
        return cnt

m = Solution()
s = 'aaa'
print m.countSubstrings(s)
