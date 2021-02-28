# https://leetcode.com/problems/permutations/

from collections import deque
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numLength = len(nums)
        subsets = []
        permutations = deque()
        permutations.append([])
        
        for currentNumber in nums:
            # we will take all existing permutations and add the current number
            # to create new permutation
            n = len(permutations)
            
            for _ in range(n):
                oldPermutation = permutations.popleft()

                # create a new permutation by adding the current number at every position
                for i in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(i, currentNumber)
                    
                    if len(newPermutation) == numLength:
                        subsets.append(newPermutation)
                    else:
                        permutations.append(newPermutation)            
        
        return subsets
