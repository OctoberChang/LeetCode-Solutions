#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start element
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if merged is empty or
            # the current does not overlap with prev, append to last
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # there's overlapping
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


