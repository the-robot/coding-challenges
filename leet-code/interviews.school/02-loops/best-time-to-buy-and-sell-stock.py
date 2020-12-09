# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        buy, sell = 0, 1

        while buy < len(prices) and sell < len(prices):
            if prices[buy] < prices[sell]:
                profits.append(prices[sell] - prices[buy])
                sell += 1
            
            elif prices[buy] >= prices[sell]:
                buy = sell
                sell += 1

        return max(profits) if len(profits) != 0 else 0
