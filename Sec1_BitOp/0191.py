#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += (n & 1)
            n >>= 1
        return ans
