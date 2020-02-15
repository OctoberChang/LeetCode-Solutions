#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def longestValidParentheses(self, s):
        if len(s) == 0: return 0

        n = len(s)
        stack = []
        dp = [0] * n

        # fill dp array
        for t, c in enumerate(s):
            if c == '(':
                stack.append((c,t))
            else:
                if len(stack) == 0:
                    continue

                # hit, so mark t and t_pre as 1
                c_pre, t_pre = stack.pop()
                dp[t], dp[t_pre] = 1, 1

        # pass dp array, and find longest consecutive 1
        print(dp)
        ans, cur = 0, 0
        for i in range(n):
            if dp[i] == 0:
                cur = 0
                continue
            cur += 1
            if cur > ans:
                ans = cur
        return ans

m = Solution()
s = ')()())'
print m.longestValidParentheses(s)
