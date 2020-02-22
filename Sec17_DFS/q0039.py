#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def combinationSum(self, candidates, target):
        ans, curr = [], []
        candidates.sort()
        self.dfs(candidates, target, 0, curr, ans)
        return ans

    def dfs(self, candidates, target, s, curr, ans):
        if target == 0:
            ans.append(list(curr))
            return

        for i in range(s, len(candidates)):
            if candidates[i] > target: break
            curr.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, curr, ans)
            curr.pop()


def Permutation(nums, d, n, used, curr, ans):
    if d == n:
        ans.append(list(curr))
        return

    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True
        curr.append(nums[i])
        Permutation(nums, d+1, n, used, curr, ans)
        curr.pop()
        used[i] = False


def Combination(nums, d, n, s, curr, ans):
    if d == n:
        ans.append(list(curr))
        return

    for i in range(s, len(nums)):
        curr.append(nums[i])
        Combination(nums, d+1, n, i+1, curr, ans)
        curr.pop()


nums = [1,2,3]
curr, ans, used = [], [], [False]*len(nums)
Permutation(nums, 0, 3, used, curr, ans)
print("Perm", ans)
curr, ans = [], []
Combination(nums, 0, 2, 0, curr, ans)
print("Comb", ans)
