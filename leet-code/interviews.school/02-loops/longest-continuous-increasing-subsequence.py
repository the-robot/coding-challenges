# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxConsecutive = boundary = 0
 
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                boundary = i

            maxConsecutive = max(maxConsecutive, i - boundary + 1)

        return maxConsecutive
