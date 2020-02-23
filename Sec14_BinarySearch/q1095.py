#!/usr/bin/env python
# encoding: utf-8

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target, mountain_arr):

        # find peak
        def binary_search(nums, left, right, check):
            while left <= right:
                mid = left + (right-left) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        n = mountain_arr.length()
        peak = binary_search(mountain_arr, 0, mountain_arr.length()-1,
                             lambda x: mountain_arr.get(x) >= mountain_arr.get(x+1))

        left = binary_search(mountain_arr, 0, peak,
                             lambda x: mountain_arr.get(x) >= target)

        if left <= peak and mountain_arr.get(left) == target:
            return left

        right = binary_search(mountain_arr, peak, mountain_arr.length()-1,
                             lambda x: mountain_arr <= target)
        if right <= mountain_arr.length-1 and mountain_arr.get(right) == target:
            return right
        return -1
