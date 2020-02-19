#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def twoSum(self, nums, target):

        hist = {}
        for idx, num in enumerate(nums):
            if num in hist:
                return [hist[num], idx]

            hist[target-num] = idx



m = Solution()
nums = [2, 7, 11, 15]
target = 9
print(m.twoSum(nums, target))
