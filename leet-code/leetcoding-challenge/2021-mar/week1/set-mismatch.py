# https://leetcode.com/problems/set-mismatch/

"""
Topic: Cyclic Sort
"""

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # sort the number using cyclic sort
        i = 0
        while i < len(nums):
            # if not sorted
            if nums[i] != i + 1:
                correctIndex = nums[i] - 1

                # if it is not the same as the number from previous index
                if nums[i] != nums[correctIndex]:
                    nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
                else:
                    i += 1
            else:
                i += 1

        # traverse the array to find the duplicate
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
            i += 1
        
        return [-1, -1]
