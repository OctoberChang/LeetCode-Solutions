#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert newInterval to the sorted one
        idx = 0
        while idx < len(intervals) and intervals[idx][0] < newInterval[0]:
            idx += 1
        intervals.insert(idx, newInterval)

        #print("intervals", intervals)
        # use q0056.py technique
        ans = []
        for start, end in intervals:
            if len(ans) == 0 or ans[-1][1] < start:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        l, r = [], []
        for interval in intervals:
            if interval[1] < start:
                l.append(interval)
            elif interval[0] > end:
                r.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        return l + [[start, end]] + r
