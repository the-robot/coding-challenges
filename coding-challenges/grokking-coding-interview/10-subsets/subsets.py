# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        # add empty subset
        subsets.append([])
        
        for num in nums:
            # take all existing substs and insert the current number in them
            # to create new subsets
            n = len(subsets)
            
            for i in range(n):
                new = list(subsets[i])
                new.append(num)
                subsets.append(new)
        
        return subsets
