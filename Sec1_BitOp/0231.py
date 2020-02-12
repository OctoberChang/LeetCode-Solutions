#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0
