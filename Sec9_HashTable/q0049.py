#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(word)
        return ans.values()
