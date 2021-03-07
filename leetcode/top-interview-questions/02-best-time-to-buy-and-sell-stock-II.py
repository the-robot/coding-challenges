from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = profit + (prices[j] - prices[i])

            i += 1
            j += 1

        return profit
        

solution = Solution()

# Test Cases
case1 = [7,1,5,3,6,4]
case2 = [1,2,3,4,5]
case3 = [7,6,4,3,1]

assert solution.maxProfit(case1) == 7
assert solution.maxProfit(case2) == 4
assert solution.maxProfit(case3) == 0
