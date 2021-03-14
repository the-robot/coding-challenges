# https://www.lintcode.com/problem/minimum-partition

from typing import List


class TopDownSolution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    def findMin(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        s = sum(nums)
        self.dp = [[-1 for x in range(s + 1)] for y in range(n)]
        return self.minRecursively(nums, 0, 0, 0)
    
    def minRecursively(self, nums: List[int], currentIndex: int, sum1: int, sum2: int) -> int:
        # base check
        if currentIndex == len(nums):
            return abs(sum1 - sum2)

        # check if it is not computed before
        if self.dp[currentIndex][sum1] == -1:
            # recursively call after including number from currentIndex in first set
            diff1 = self.minRecursively(nums, currentIndex + 1, sum1 + nums[currentIndex], sum2)

            # recursively call after including number from currentIndex in second set
            diff2 = self.minRecursively(nums, currentIndex + 1, sum1, sum2 + nums[currentIndex])

            self.dp[currentIndex][sum1] = min(diff1, diff2)

        return self.dp[currentIndex][sum1]


class BottomUpSolution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    def findMin(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        s = sum(nums)
        dp = [[False for x in range(int(s/2) + 1)] for y in range(n)]

        # populate the s = 0 columns, as we can always form '0' sum with an empty set
        for i in range(n):
            dp[i][0] = True
        
        # with only one number, we can form a subset only when the required sum is equal to that number
        for j in range(0, int(s/2) + 1):
            dp[0][j] = nums[0] == j
        
        # process all the sub-arrays for all sum
        for i in range(1, n):
            for j in range(1, int(s/2) + 1):
                # if we can get the sum 's' without the number at index 'i'
                if dp[i - 1][j]:
                    dp[i][j] = True
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]
        
        sum1 = 0
        # find the largest index in the last row which is true
        for i in range(int(s/2), -1, -1):
            if dp[n - 1][i]:
                sum1 = i
                break
        
        sum2 = s - sum1
        return abs(sum2 - sum1)
