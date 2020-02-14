#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = n-2
        while left >= 0:
            if nums[left] < nums[left+1]: break
            left -= 1

        # already sorted reversely, the largest permutation,
        # so return the smallest perm, which is sort ascending.
        if left < 0:
            nums.sort()
            return

        right = left+1
        while right < n and nums[right] > nums[left]:
            right += 1

        # switch left and right
        nums[left], nums[right-1] = nums[right-1], nums[left]
        nums[left+1:] = nums[left+1:][::-1]
        print(nums)
        return


m = Solution()
nums = [1, 2, 4, 3, 1]
m.nextPermutation(nums)



