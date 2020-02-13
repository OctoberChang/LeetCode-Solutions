#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()

        best_sum = -1
        best_delta = float("+inf")
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_delta = abs(target-cur_sum)
                # lucky case
                if cur_sum == target:
                    return cur_sum

                if cur_delta < best_delta:
                    best_sum = cur_sum
                    best_delta = cur_delta

                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1
        return best_sum

m = Solution()
m.threeSumClosest([-1, 2, 1, -4], 1)
