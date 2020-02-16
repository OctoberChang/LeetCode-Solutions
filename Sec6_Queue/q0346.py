#!/usr/bin/env python
# encoding: utf-8


from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.size = size
        self.sum = 0.0

    def next(self, val: int) -> float:
        if len(self.q) < self.size:
            self.sum += val
            self.q.append(val)
            return self.sum / float(len(self.q))
        else:
            remove_val = self.q.popleft()
            self.sum += -remove_val + val
            self.q.append(val)
            return self.sum / float(len(self.q))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
