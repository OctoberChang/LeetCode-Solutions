#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # find max({x | x: P[y] - P[x] >= K })

        # compute presum array
        n = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        ans = float("+inf")
        monoq = collections.deque() # from smallest to largest, store its idx
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()
            while monoq and Py - P[monoq[0]] >= K:
                x = monoq.popleft()
                ans = min(ans, y - x)
            monoq.append(y)

        # return ans
        return ans if ans != float("+inf") else -1

