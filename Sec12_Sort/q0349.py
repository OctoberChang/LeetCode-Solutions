#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # let's assume len(nums1) > len(nums2)
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        # build lookup table for nums1
        lookup = set(nums1)

        ans = []
        for num in nums2:
            if num in lookup:
                ans.append(num)
                lookup.remove(num)

        return ans



