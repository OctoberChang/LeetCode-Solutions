#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency matrix of the directed graph
        self.graph = collections.defaultdict(list)
        for to_node, from_node in prerequisites:
            self.graph[from_node].append(to_node)

        # node's state: 0=unk; 1=visiting; 2=visited
        self.state = [0] * numCourses

        # post visiting order
        self.order = []

        for node in range(numCourses):
            if self.dfs_is_cycle(node):
                return []

        return self.order[::-1]

    def dfs_is_cycle(self, curr_node):
        if self.state[curr_node] == 1: return True
        if self.state[curr_node] == 2: return False

        # visiting curr_node
        self.state[curr_node] = 1
        for next_node in self.graph[curr_node]:
            if self.dfs_is_cycle(next_node):
                return True

        # no cycle so far, mark curr_node as visited
        # and append curr_node to the post-order traverse list
        self.state[curr_node] = 2
        self.order.append(curr_node)
        return False

