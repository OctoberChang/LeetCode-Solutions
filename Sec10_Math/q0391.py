#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area_sum = 0.0
        for rec in rectangles:
            # four corner
            p1 = (rec[0], rec[1])
            p2 = (rec[2], rec[1])
            p3 = (rec[2], rec[3])
            p4 = (rec[0], rec[3])
            for p in [p1, p2, p3, p4]:
                if p not in corners:
                    corners.add(p)
                else:
                    corners.remove(p)

            area_sum += (p3[0] - p1[0]) * (p3[1] - p1[1])

        # check if there are four corner
        if len(corners) != 4: return False

        # check if area_sum equal to area
        corners = sorted(corners)
        x1, y1 = corners[0]
        x2, y2 = corners[-1]
        return area_sum == (x2-x1)*(y2-y1)


