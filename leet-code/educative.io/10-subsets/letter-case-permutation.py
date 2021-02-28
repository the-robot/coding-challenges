# https://leetcode.com/problems/letter-case-permutation/

from collections import deque
from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        lenS = len(S)
        permutations = [S]
        
        # process every character of the string one by one
        for i in range(lenS):
            if S[i].isalpha(): # only process character and skip digits
                n = len(permutations)
                
                for j in range(n):
                    newPermutation = list(permutations[j])
                    
                    # swap character
                    newPermutation[i] = newPermutation[i].swapcase()
                    
                    permutations.append("".join(newPermutation))
        
        return permutations


# Alternative solution similar to permutations.py using deque
class AlternativeSolution:
    def letterCasePermutation(self, S: str) -> List[str]:
        lenS = len(S)
        subsets = []
        permutations = deque()
        permutations.append("")
        
        for char in S:
            n = len(permutations)
            
            for _ in range(n):
                oldPermutation = permutations.popleft()
                iterationLimit = 2 if char.isalpha() else 1
                
                for i in range(iterationLimit):
                    newPermutation = oldPermutation
                    newPermutation += char.lower() if i == 0 else char.upper()

                    if len(newPermutation) == lenS:
                        subsets.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
        
        return subsets
