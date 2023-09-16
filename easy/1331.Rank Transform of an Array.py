# https://leetcode.com/problems/rank-transform-of-an-array/description/

from typing import List

def arrayRankTransform(arr: List[int]) -> List[int]:
    rank = {val:idx+1 for idx,val in enumerate(sorted(set(arr)))}
    
    return list(map(rank.get,arr))


assert arrayRankTransform([40,10,20,30]) == [4,1,2,3]
assert arrayRankTransform([100,100,100]) == [1,1,1]
assert arrayRankTransform([37,12,28,9,100,56,80,5,12]) == [5,3,4,2,8,6,7,1,3]
