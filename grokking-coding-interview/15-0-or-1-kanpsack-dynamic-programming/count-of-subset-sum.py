# https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

from typing import List

class Solution:
    def countSubsets(self, nums: List[int], sum: int) -> int:
        n = len(nums)

        if n == 0:
            return 0

        self.dp = [[-1 for x in range(sum + 1)] for y in range(n)]

        return self.count(nums, sum, 0)
    
    def count(self, nums: List[int], sum: int, currentIndex: int) -> int:
        # base case
        if sum == 0:
            return 1

        if currentIndex >= len(nums):
            return 0
        
        # check if it is not computed before
        if self.dp[currentIndex][sum] == -1:
            # recursively compute the sum of subset with current index
            # if the number at current index does not exceed the sum
            sum1 = 0
            if nums[currentIndex] <= sum:
                sum1 = self.count(nums, sum - nums[currentIndex], currentIndex + 1)
            
            # recursive compute the sum of subset without current index
            sum2 = self.count(nums, sum, currentIndex + 1)

            self.dp[currentIndex][sum] = sum1 + sum2
    
        return self.dp[currentIndex][sum]


if __name__ == "__main__":
    s = Solution()

    print(s.countSubsets([1, 1, 2, 3], 4))
    print(s.countSubsets([1, 2, 7, 1, 5], 9))
