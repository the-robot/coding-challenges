# https://leetcode.com/problems/missing-number/

from typing import List

# https://www.geeksforgeeks.org/find-the-missing-number/

"""
Hypothesis is simple, assume we have an array [3, 0, 1]

0 ^ 1 ^ 2 ^ 3 = 0 ^ 1 ^ (missing number) ^ 3

0 ^ 1 ^ 2 ^ 3 -> 0
0 ^ 1 ^ 3 -> 2
so we do 0 ^ 2 -> 2, it is the missing number
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        
        # x1 represents XOR of all values in [0, N]
        x1 = 0
        for index in range(0, N + 1): # + 1 because in range N is exclusive
            x1 ^= index

        # x2 represents XOR of all values in nums
        x2 = 0
        for num in nums:
            x2 ^= num

        # missing number is the XOR of x1 and x2
        return x1 ^ x2
