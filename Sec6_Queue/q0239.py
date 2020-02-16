#!/usr/bin/env python
# encoding: utf-8

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        dq = deque()
        results = []
        for i in range(n):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i - k + 1 >= 0: ans.append(nums[dp[0]])
            if i - k + 1 >= dq[0]:
                dq.popleft()



