#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, cur = set(), []
        candidates.sort()
        self.dfs(candidates, target, 0, cur, ans)
        return ans

    def dfs(self, candidates, target, s, cur, ans):
        if target == 0:
            ans.add(tuple(cur))
            return

        for i in range(s, len(candidates)):
            if candidates[i] > target: break
            cur.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, cur, ans)
            cur.pop()

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, cur = [], []
        candidates.sort()
        self.dfs(candidates, target, 0, cur, ans)
        return ans

    def dfs(self, candidates, target, s, cur, ans):
        if target == 0:
            ans.append(list(cur))
            return

        for i in range(s, len(candidates)):
            if candidates[i] > target: break
            if i > s and candidates[i] == candidates[i-1]: continue
            cur.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, cur, ans)
            cur.pop()


