#!/usr/bin/env python
# encoding: utf-8

class Solution:

    def __init__(self, nums: List[int]):
        self.__nums = nums


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.__nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = list(self.__nums)

        cur_idx = len(self.__nums) - 1
        while cur_idx > 0:
            rand_idx =random.randint(0, cur_idx)
            nums[cur_idx], nums[rand_idx] = nums[rand_idx], nums[cur_idx]
            cur_idx -= 1
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
