# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

from typing import List

def finalPrices(prices: List[int]) -> List[int]:
    stack = []
    
    for i in range(len(prices)):

        while stack and (prices[stack[-1]] >= prices[i]):
            prices[stack.pop()] -= prices[i]
        
        stack.append(i)

    return prices


assert finalPrices([8,4,6,2,3]) == [4,2,4,2,3]
assert finalPrices([1,2,3,4,5]) == [1,2,3,4,5]
assert finalPrices([10,1,1,6]) == [9,0,1,6]
