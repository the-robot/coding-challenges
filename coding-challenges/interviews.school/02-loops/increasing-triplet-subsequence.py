# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstSmallest = secondSmallest = float("inf")

        for num in nums:
            if num <= firstSmallest:
                firstSmallest = num
            elif num <= secondSmallest:
                secondSmallest = num
            else:
                return True

        return False
