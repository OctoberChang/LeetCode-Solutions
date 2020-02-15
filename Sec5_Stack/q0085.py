#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def maxHistArea(self, dp):
        n = len(dp)
        stack, max_area, i = [], 0, 0
        while i <= n:
            if not stack or (i < n and dp[stack[-1]] < dp[i]):
                stack.append(i)
                i += 1

            last = stack.pop()
            if not stack:
                max_area = max(max_area, dp[last] * i)
            else:
                max_area = max(max_area, dp[last] * (i - stack[-1] -1))
        return max_area

    def maximalRectangle(self, matrix):
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [0] * n
        max_area = -1
        for i in range(m):
            # init dp for max rectangle of histogram sub-prob
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[j] = 0
                else:
                    dp[j] += matrix[i][j]
            # call sub-problem solver
            max_area = max(max_area, self.maxHistArea(dp))
        return max_area


