#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def isPalindrome(self, s):
        n = len(s)

        l, r = 0, n-1
        while l < r:
            # if s[l] or s[r] is not number, move the ptr,
            # and continue to next round
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            # now the s[l] and s[r] are all numbers, check
            if s[l].lower() != s[r].lower():
                break
            else:
                l += 1
                r -= 1

        print(l, r)
        if l >= r:
            return True
        else:
            return False


m = Solution()

s = "A man, a plan, a canal: Panama"
s = "babcab"
s = "race a car"
print m.isPalindrome(s)
