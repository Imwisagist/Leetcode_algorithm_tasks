# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

def maxProfit(prices: List[int]) -> int:
    buy, profit = prices[0], 0

    for x in prices[1:]:
        buy = min(buy, x)
        profit = max(profit, x - buy)

    return profit


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 5, 4, 2, 1]) == 0
