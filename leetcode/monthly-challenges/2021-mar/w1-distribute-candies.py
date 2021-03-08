# https://leetcode.com/problems/distribute-candies/

from typing import List

"""
Topic: Sets
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        totalCandies = len(candyType)
        uniqueCandies = set()
        
        for candy in candyType:
            uniqueCandies.add(candy)
        
        return min(len(uniqueCandies), totalCandies // 2)
