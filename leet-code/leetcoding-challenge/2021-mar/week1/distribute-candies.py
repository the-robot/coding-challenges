# https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/

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
