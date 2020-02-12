#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 0001 XOR 0000 = 0001
        # a XOR 0 = a
        # a XOR a = 0
        # a XOR b XOR a = a XOR a XOR b = b

        a = 0
        for num in nums:
            a ^= num
        return a
