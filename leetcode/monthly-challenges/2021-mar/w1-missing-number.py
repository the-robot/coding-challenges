# https://leetcode.com/problems/missing-number/

from typing import List

"""
Topic: Cyclic Sort
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort the number
        i = 0
        while i < len(nums):
            correctIndex = nums[i]

            # do not sort nums[i] >= len(nums) because we do not have
            # space for that and these are number sitting in wrong place
            if nums[i] < len(nums) and nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1
        
        # traverse the array
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            i += 1
        
        return len(nums)
