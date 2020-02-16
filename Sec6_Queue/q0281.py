#!/usr/bin/env python
# encoding: utf-8

import collections


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self) -> int:
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self) -> bool:
        return bool(self.q)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

v1 = [1,2]
v2 = [3,4,5,6]
it, v = ZigzagIterator(v1, v2), []
print(it.q)
