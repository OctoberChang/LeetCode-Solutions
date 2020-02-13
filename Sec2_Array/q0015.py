#!/usr/bin/env python
# encoding: utf-8

import bisect

class Solution:
    def threeSumTLE(self, nums):

        # sort from smallest to largest, O(nlogn)
        n = len(nums)
        nums.sort()

        # two pointer
        ans = []
        seen_dict = {}
        for i in range(0, n-2):
            j = n-1
            while j > i+1:
                bs_val = 0 - (nums[i] + nums[j])
                # binary search the insertion position of val between nums[lo:hi]
                # return idx s.t. nums[lo:idx] < val and nums[idx:hi] >= val
                bs_idx = bisect.bisect_left(nums, bs_val,  i+1, j)
                if bs_idx >= j:
                    j -= 1
                    continue

                # search hit
                cand = [nums[i], bs_val, nums[j]]
                cand_str = str(cand)
                #print("a[i={}]={} a[j={}]={} x={} idx={} val={}".format(
                #    i, nums[i], j, nums[j], bs_val, bs_idx, nums[bs_idx]))
                if nums[bs_idx] == bs_val and not cand_str in seen_dict:
                    ans.append(cand)
                    seen_dict[cand_str] = cand
                    print(i, j, cand)
                j -= 1
        return ans

    def threeSum(self, nums):
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j, k = j+1, k-1
                    while j < k and nums[j] == nums[j-1]: j+= 1
                    while j < k and nums[k] == nums[k+1]: k-= 1
        print(ans)
        return ans


nums = [-1, 0, 1, 2, -1, -4]
#nums = [-1,0,1,0]
#nums = [0,-4,-1,-4,-2,-3,2]
m = Solution()
m.threeSum(nums)
