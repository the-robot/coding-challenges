# https://leetcode.com/problems/single-number

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        
        # x1 represents XOR of all values in [0, N]
        x1 = 0
        for index in range(0, N + 1): # + 1 because in range N is exclusive
            x1 ^= index ^ index
        
        # x2 represents XOR of all values in nums
        x2 = 0
        for num in nums:
            x2 ^= num
        
        # single number is the XOR of x1 and x2
        return x1 ^ x2
