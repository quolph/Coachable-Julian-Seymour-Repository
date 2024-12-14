from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max_price = prices[0]
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = max_price = price
            elif price > max_price:
                max_price = price
                profit = max(profit, max_price - min_price)
        return profit
    def maxProfitSlow(self, prices: List[int]) -> int:
        pm = 0
        i = 0
        min_price = prices[0]
        while i < len(prices) - 1 and prices[i] >= prices[i+1]:
            prices.pop(i)
        i = len(prices) - 1
        while len(prices) - 1 > 1 and prices[len(prices)-1] <= prices[len(prices)-2]:
            prices.pop(len(prices)-1)
        i = 0
        min_price = float("inf")
        while i < len(prices) - 1:
            if prices[i] >= min_price:
                i += 1
                continue
            min_price = prices[i]
            j = i + 1
            while j < len(prices):
                temp_pm = prices[j] - prices[i]
                if temp_pm > 0:
                    pm = max(pm, temp_pm)
                j += 1
            i += 1
        return pm
