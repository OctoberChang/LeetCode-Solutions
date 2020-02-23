#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        ans, left, right = float('-inf'), 0, n-1

        while left < right:
            if height[left] < height[right]:
                ans = max(ans, height[left] * (right - left))
                left += 1
            else:
                ans = max(ans, height[right] * (right - left))
                right -= 1

        return ans

