#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def foursum(self, nums, target):
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n-3):
            # avoid duplicate in i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, n-2):
                # avoid duplicate in j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j+1, n-1
                while k < l:
                    #print(i, j, k, l)
                    cur_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    # lucky case
                    if cur_sum == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k, l = k + 1, l-1
                        while k < l and nums[k] == nums[k-1]: k += 1
                        while k < l and nums[l] == nums[l+1]: l -= 1
                    elif cur_sum < target:
                        k += 1
                    elif cur_sum > target:
                        l -= 1
        print(ans)
        return ans

#
m = Solution()
m.foursum([1, 0, -1, 0, -2, 2], 0)

