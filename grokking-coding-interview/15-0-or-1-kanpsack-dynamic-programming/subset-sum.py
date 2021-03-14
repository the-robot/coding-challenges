# https://www.educative.io/courses/grokking-the-coding-interview/gxrnL0GQGqk

from typing import List


class Solution:
    def canPartition(self, nums: List[int], sum: int) -> bool:
        # basic checks
        n = len(nums)
        dp = [[False for x in range(sum + 1)] for y in range(n)]

        # populate the sum = 0 columns, as we can always form '0' sum with an empty set
        for i in range(0, n):
            dp[i][0] = True
        
        # with only one number, we can form a subset only when the required sum is equal
        # to its value.
        for j in range(1, sum + 1):
            dp[0][j] = nums[0] == j
        
        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for j in range(1, sum + 1):
                # if we can get the sum 's' without the number at index 'i'
                # at current index 'i', it will also be true.
                if dp[i-1][j]:
                    dp[i][j] = True

                # if sum is >= the current number at index 'i', see if we can find a subset
                # to get the remaining sum.
                #
                # if sum < the current number at index 'i', it is exceeded already and there's no way
                # we can find one.
                elif j >= nums[i]:
                    # if we can find a j - current number at index 'i' means, this one is true
                    # because that previous combination + current number will be equal to sum.
                    dp[i][j] = dp[i-1][j - nums[i]]

        # else include the number and see if we can find a subset to get the remaining sum.
        return dp[n-1][sum]


if __name__ == "__main__":
    s = Solution()

    print(s.canPartition([1, 2, 3, 7], 6))
    print(s.canPartition([1, 2, 7, 1, 5], 10))
    print(s.canPartition([1, 3, 4, 8], 6))
