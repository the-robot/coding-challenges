# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]
        
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:        
        return self.sums[j+1] - self.sums[i]
