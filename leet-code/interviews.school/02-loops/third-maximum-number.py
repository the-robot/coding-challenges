# https://leetcode.com/problems/third-maximum-number/

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums)) # remove duplicates

        # edge conditions (if there's no third maximum means return first maximum)
        if len(nums) <= 2:
            return max(nums)

        firstMaximum = max(nums[0], nums[1])
        secondMaximum = min(nums[0], nums[1])
        thirdMaximum = None

        i = 2
        while i < len(nums):
            if nums[i] > firstMaximum:
                thirdMaximum = secondMaximum
                secondMaximum = firstMaximum
                firstMaximum = nums[i]

            elif nums[i] > secondMaximum:
                thirdMaximum = secondMaximum
                secondMaximum = nums[i]

            elif thirdMaximum is None or nums[i] > thirdMaximum:
                thirdMaximum = nums[i]

            i += 1

        return thirdMaximum
