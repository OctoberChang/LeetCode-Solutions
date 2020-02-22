#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur, ans = [], []
        nums = list(range(1,n+1))
        self.dfs(nums, k, 0, 0, cur, ans)
        return ans

    def dfs(self, nums, k, d, s, cur, ans):
        if d == k:
            ans.append(list(cur))
            return

        for i in range(s, len(nums)):
            cur.append(nums[i])
            self.dfs(nums, k, d+1, i+1, cur, ans)
            cur.pop()

