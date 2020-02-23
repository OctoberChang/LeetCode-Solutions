#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        moves = \
            [[ 1, 2], [ 1,-2], [ 2, 1], [ 2, -1], \
             [-1, 2], [-1,-2], [-2, 1], [-2, -1]]

        dp_old = [[0 for _ in range(N)] for _ in range(N)]
        dp_old[r][c] = 1

        for k in range(K):
            dp_new = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for m in range(8):
                        x, y = j + moves[m][0], i + moves[m][1]
                        if x < 0 or x >= N or y < 0 or y >= N: continue

                        dp_new[y][x] += dp_old[j][i]

            dp_old, dp_new = dp_new, dp_old

        ans = 0.0
        for i in range(N):
            for j in range(N):
                ans += dp_old[j][i]
        return ans / float(8**K)


