#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        lookup = collections.defaultdict(int)
        for c in s:
            lookup[c] += 1

        for c in t:
            if lookup[c] <= 0:
                return False
            lookup[c] -= 1
        return True
