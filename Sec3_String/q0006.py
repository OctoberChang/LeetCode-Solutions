#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def convert(self, s, numRows):
        n = len(s)

        ret_ans = [[] for _ in range(numRows)]
        cur_row = 0
        going_down = True
        for i in range(n):
            ret_ans[cur_row] += s[i]
            if numRows == 1:
                continue

            if going_down:  # going down case
                if cur_row == numRows-1:
                    going_down = False
                    cur_row -= 1
                else:
                    cur_row += 1
            else:   # going up case
                if cur_row == 0:
                    going_down = True
                    cur_row += 1
                else:
                    cur_row -= 1

        ans = ''
        for s_i in ret_ans:
            ans += ''.join(s_i)
        return ans




m = Solution()
s, numRows = 'PAYPALISHIRING', 3
s, numRows = 'ABC', 1
print m.convert(s, numRows)

