#!/usr/bin/env python
# encoding: utf-8

import collections

class Solution:
    def findItinerary(self, tickets):

        # sub-routine
        def route_helper(origin, n_edge, graph, ans):
            if n_edge == 0:
                return True

            for i, (dest, valid) in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False
                    ans.append(dest)
                    if route_helper(dest, n_edge-1, graph, ans):
                        return ans
                    ans.pop()
                    graph[origin][i][1] = True
            return False

        # dict: key is str, val is list[str]
        graph = {}
        graph = collections.defaultdict(list)
        for v_1, v_2 in tickets:
            graph[v_1].append([v_2, True])

        # sort val_list in lookup table
        print("graph", graph)
        for key in graph.keys():
            graph[key].sort()

        ans = ['JFK']
        route_helper('JFK', len(tickets), graph, ans)
        return ans

m = Solution()
#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print(m.findItinerary(tickets))
