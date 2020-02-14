#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 1:
            return 1

        ans = 1
        i, j = 0, 1
        while j < n:
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
                j += 1
                ans += 1

        print(ans)
        print(nums)

#
m = Solution()
nums = [0, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
m.removeDuplicates(nums)

