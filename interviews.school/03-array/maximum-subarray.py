# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            """
            finding max is to decide whether the current number
            should add with the number behind
            if the sum is higher; take the sum (num[i-1]) + nums[i]
            else take it's own number (nums[i])
            
            I.e. [-2, 1, -3, 4, -1, 2, 1, -5, 4] will become
                 [-2, 1, -2, 4,  3, 5, 6,  1, 5].
                 
                 there are four consecutives.
                 [-2] [1, -2] [4, 3, 5, 6] and [1, 5]
                 
                 we find the highest number which means it results from
                 the consecutive with highest sum [4, 3, 5, 6].
            """
            nums[i] = max(nums[i-1] + nums[i], nums[i])
    
        return max(nums)
