#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if len(graph[0]) == 0: return []

        ans, curr = [], []
        self.n = len(graph)
        self.graph = graph
        self.dfs(0, curr, ans)
        return ans

    def dfs(self, node, curr, ans):
        if node == self.n-1:
            curr.append(self.n-1)
            ans.append(list(curr))
            curr.pop()
            return

        curr.append(node)
        for next_node in self.graph[node]:
            self.dfs(next_node, curr, ans)
        curr.pop()
        return

