#!/usr/bin/env python
# encoding: utf-8

from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []

        def push(i, j):
            if i < n and j < n:
                heappush(min_heap, [matrix[j][i], i, j])

        push(0, 0)
        while min_heap and k > 0:
            kth_smallest, i, j = heappop(min_heap)
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
            k -= 1

        return kth_smallest
