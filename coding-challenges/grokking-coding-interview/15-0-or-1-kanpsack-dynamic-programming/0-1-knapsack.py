# https://www.educative.io/courses/grokking-the-coding-interview/gkZNLjV2kBk

from typing import List


class TopDownSolution:
    def solveKnapsack(self, profits: List[int], weights: List[int], capacity: int) -> int:
        # create a two dimensional array for Memoization, each element is initialized to '-1'
        dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
        return self.knapsack(dp, profits, weights, capacity, 0)
    
    def knapsack(
        self, dp: List[List[int]], profits: List[int], weights: List[int], capacity: int, currentIndex: int
    ) -> int:
        # base check
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        # if we have already solved the similar problem, return the result from memory
        if dp[currentIndex][capacity] != -1:
            return dp[currentIndex][capacity]
        
        # recursively call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity,
        # we shouldn't process this
        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + self.knapsack(
                dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1,
            )
        
        # recursive call after excluding the element at the currentIndex
        profit2 = self.knapsack(dp, profits, weights, capacity, currentIndex + 1)

        # save the value in dp
        dp[currentIndex][capacity] = max(profit1, profit2)

        return dp[currentIndex][capacity]


class BottomUpSolution:
    def solveKnapsack(self, profits: List[int], weights: List[int], capacity: int) -> int:
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0
        
        dp = [[0 for x in range(capacity + 1)] for y in range(n)]

        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0
        
        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = profits[0]
        
        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity + 1):
                profit1, profit2 = 0, 0

                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i - 1][c - weights[i]]

                # exclude the item
                profit2 = dp[i - 1][c]

                # take maximum
                dp[i][c] = max(profit1, profit2)

        # maximum profit will be at the bottom-right corner
        return dp[n - 1][capacity]


if __name__ == "__main__":
    s = BottomUpSolution()

    print(s.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(s.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
