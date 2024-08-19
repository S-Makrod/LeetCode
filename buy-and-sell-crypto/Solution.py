from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        largest = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            val = prices[i]
            max_profit = max(max_profit, largest - val)
            largest = max(largest, val)

        return max_profit