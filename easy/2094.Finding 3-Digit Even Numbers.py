# https://leetcode.com/problems/finding-3-digit-even-numbers/description/

from typing import List
from collections import Counter

def findEvenNumbers(digits: List[int]) -> List[int]:
    c = Counter(digits)
    
    return [
        i*100 + j*10 + k 
        for i in range(1,10) 
        for j in range(0,10) 
        for k in range(0,10,2) 
        if c[i]>0 and c[j]>(i==j) and c[k]>(k==i)+(k==j)
    ]


assert findEvenNumbers([2,1,3,0]) == [102,120,130,132,210,230,302,310,312,320]
assert findEvenNumbers([2,2,8,8,2]) == [222,228,282,288,822,828,882]
assert findEvenNumbers([3,7,5]) == []
