#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        if L + M > n: return 0

        # presum array
        # P[j] - P[i-1] = sum(A[i:j])
        P = [A[0]]
        for i in range(1, n):
            P.append(P[-1] + A[i])

        # init var
        ans, max_L, max_M = P[L+M-1], P[L-1], P[M-1]
        for t in range(L+M, n):
            max_L = max(max_L, P[t-M] - P[t-M-L])
            max_M = max(max_M, P[t-L] - P[t-L-M])
            ans = max(ans,
                      max_L + P[t] - P[t-M],
                      max_M + P[t] - P[t-L])

        return ans
