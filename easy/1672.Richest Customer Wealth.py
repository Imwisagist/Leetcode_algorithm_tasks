# https://leetcode.com/problems/richest-customer-wealth/

from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    
    return max(sum(acc) for acc in accounts) 


assert maximumWealth([[1,2,3],[3,2,1]]) == 6
assert maximumWealth([[1,5],[7,3],[3,5]]) == 10
assert maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17
