#!/usr/bin/env python
# encoding: utf-8

def singleNumber(nums):
    hash_table = {}
    for num in nums:
        if num not in hash_table:
            hash_table[num] = 1
        else:
            hash_table[num] += 1

    for key in hash_table:
        if hash_table[key] == 1:
            return key


nums = [2,2,3,2]
print(singleNumber(nums))
