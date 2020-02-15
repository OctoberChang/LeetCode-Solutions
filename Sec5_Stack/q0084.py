#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def largestRectangleArea(self, heights):

        stack, max_area = [], 0
        i = 0
        while i <= len(heights):
            if not stack or (i < len(heights) and heights[stack[-1]] < heights[i]):
                stack.append(i)
                i += 1

            else:
                last = stack.pop()
                if stack:
                    max_area = max(max_area, heights[last] * (i - stack[-1] - 1))
                else:
                    max_area = max(max_area, heights[last] * i)
        return max_area


m = Solution()

heights = [3, 1, 3, 2, 2]
print m.largestRectangleArea(heights)
