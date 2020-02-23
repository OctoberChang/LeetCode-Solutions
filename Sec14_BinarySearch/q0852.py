#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        left, right = 0, len(A)-1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] > A[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left
