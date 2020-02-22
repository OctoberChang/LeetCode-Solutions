#!/usr/bin/env python
# encoding: utf-8


import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        curr_count = collections.defaultdict(int)
        expt_count = collections.defaultdict(int)
        for char in t:
            expt_count[char] += 1

        l, r, cnt, min_l, min_w = 0, 0, 0, 0, float('inf')
        while r < len(s):
            # update count
            curr_count[s[r]] += 1
            if curr_count[s[r]] <= expt_count[s[r]]:
                cnt += 1

            # find a valid window
            if cnt == len(t):
                # moving left ptr
                while expt_count[s[l]] == 0 or curr_count[s[l]] > expt_count[s[l]]:
                    curr_count[s[l]] -= 1
                    l += 1
                # update min_w and min_l ptr
                if min_w > r - l + 1:
                    min_l = l
                    min_w = r - l + 1

            # update right ptr
            r += 1

        if min_w == float("inf"):
            return ""
        return s[min_l:min_l+min_w]
