# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        # if 's' is an odd number, we can't have two subsets with equal sum
        if s % 2 != 0:
            return False
        
        # initialize the 'dp' array, None for default, True if subset is valid and False if not
        dp = [[None for x in range(int(s/2) + 1)] for y in range(len(nums))]
    
        return self.partition(dp, nums, int(s/2), 0)

    def partition(self, dp: List[List[int]], nums: List[int], sum: int, currentIndex: int) -> bool:
        # base check
        if sum == 0:
            return True
    
        n = len(nums)
        if n == 0 or currentIndex >= n:
            return False
    
        # if we have not already processed a similar problem
        if dp[currentIndex][sum] == None:
            # recursive call after choosing the number at the 'currentIndex'
            # if the number at 'currentIndex' exceeds the sum, we should'nt process this
            if nums[currentIndex] <= sum:
                if self.partition(dp, nums, sum - nums[currentIndex], currentIndex + 1):
                    dp[currentIndex][sum] = True
                    return True
    
        # recursive call after excluding the number at the 'currentIndex'
        dp[currentIndex][sum] = self.partition(dp, nums, sum, currentIndex + 1)
        return dp[currentIndex][sum]
