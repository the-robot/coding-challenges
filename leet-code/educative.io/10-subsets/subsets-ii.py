# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)
        
        subsets = []
        
        # add empty subset
        subsets.append([])
        
        startIndex, endIndex = 0, 0
        
        for i in range(len(nums)):
            startIndex = 0
            
            # if current and previous are same, create new subset only from the subsets
            # added in the previous step
            if i > 0 and nums[i] == nums[i-1]:
                startIndex = endIndex + 1
            
            endIndex = len(subsets) - 1
            
            for j in range(startIndex, endIndex + 1):
                # create a new subset from the existing subset and add the current element to it
                new = list(subsets[j])
                new.append(nums[i])
                subsets.append(new)
        
        return subsets
