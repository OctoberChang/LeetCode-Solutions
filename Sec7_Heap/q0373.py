#!/usr/bin/env python
# encoding: utf-8

import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        ans = []
        if len(nums1) > len(nums2):
            for pair in self.kSmallestPairs(nums2, nums1, k):
                ans.append([pair[1], pair[0]])
            return ans

        min_heap = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(min_heap, [nums1[i]+nums2[j], i, j])

        push(0, 0)
        while min_heap and len(ans) < k:
            _, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, j)
            print(min_heap)
        return ans


m = Solution()
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(m.kSmallestPairs(nums1, nums2, k))

