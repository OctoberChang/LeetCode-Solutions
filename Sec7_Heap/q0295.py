#!/usr/bin/env python
# encoding: utf-8

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # note that heapq default is a min-heap!!!
        # to simulate a max-heap, flip the value by negative sign
        # we require len(max_heap) = len(min_heap) or len(max_heap) = len(min_heap) + 1
        # otherwise, re-balance the two side
        self.__max_heap = []    # store smaller half
        self.__min_heap = []    # store larger half


    def addNum(self, num: int) -> None:
        if not self.__max_heap:
            heappush(self.__max_heap, -num)

        elif num < -self.__max_heap[0]:
            heappush(self.__max_heap, -num)
            if len(self.__max_heap) > len(self.__min_heap) + 1:
                heappush(self.__min_heap, -heappop(self.__max_heap))
        else:
            heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap):
                heappush(self.__max_heap, -heappop(self.__min_heap))

    def findMedian(self) -> float:
        if len(self.__max_heap) == len(self.__min_heap):
            return ( -self.__max_heap[0] + self.__min_heap[0] ) / 2.0
        else:
            return -self.__max_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
