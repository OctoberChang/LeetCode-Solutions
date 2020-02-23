#!/usr/bin/env python
# encoding: utf-8

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0

        intervals.sort()
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])
        for interval in intervals[1:]:
            if min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        return len(min_heap)


