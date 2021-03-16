# https://leetcode.com/problems/target-sum/

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        # the reason we have to use map instead of an array is because
        # the sum can be negative also
        self.dp = [{} for y in range(n)]
        return self.find(nums, S, 0, 0)

    def find(self, nums: List[int], S: int, currentIndex: int, currentSum: int) -> int:
        if currentIndex == len(nums):
            return 1 if currentSum == S else 0

        if currentSum not in self.dp[currentIndex]:
            positive = self.find(nums, S, currentIndex + 1, currentSum + nums[currentIndex])
            negative = self.find(nums, S, currentIndex + 1, currentSum - nums[currentIndex])

            self.dp[currentIndex][currentSum] = positive + negative

        return self.dp[currentIndex][currentSum]
