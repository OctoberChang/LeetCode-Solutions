#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        cur, ans = [], []
        nums = list(range(1, n+1))
        self.dfs(nums, k, 0, 0, cur, ans)
        return ans

    def dfs(self, nums, k, d, s, cur, ans):
        if d == k and sum(cur) == len(nums):
            ans.append(list(cur))
            return

        for i in range(s, len(nums)):
            if nums[i] > 9: continue
            cur.append(nums[i])
            self.dfs(nums, k, d+1, i+1, cur, ans)
            cur.pop()
