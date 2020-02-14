#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        if n == 1:
            if nums[0] != val: return 1
            else: return 0

        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        print(i)
        print(nums)

#
m = Solution()
nums, val = [3, 2, 2, 3], 3
#nums, val = [0,1,2,2,3,0,4,2], 2
#nums = [0,0,1,1,1,2,2,3,3,4]
m.removeElement(nums, val)

