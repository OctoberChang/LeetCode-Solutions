#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency matrix of the directed graph
        self.graph = collections.defaultdict(list)
        for to_node, from_node in prerequisites:
            self.graph[from_node].append(to_node)

        # node's state: 0=unknown; 1=visiting; 2=visited
        self.state = [0] * numCourses

        # check if there's cycle
        for n in range(numCourses):
            if self.dfs_is_cycle(n):
                return False
        # no cycle, then success
        return True

    def dfs_is_cycle(self, node):
        if self.state[node] == 1: return True
        if self.state[node] == 2: return False

        # mark node as visiting
        self.state[node] = 1

        # traverse its neighbor's node
        for next_node in self.graph[node]:
            if self.dfs_is_cycle(next_node):
                return True

        self.state[node] = 2
        return False

