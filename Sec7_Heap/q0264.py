#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0: return 0

        seen = {1, }
        heap = []
        heapq.heappush(heap, 1)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            for i in [2, 3, 5]:
                new_ugly = ugly_number * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly_number

