# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

from collections import defaultdict
from typing import List


def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    grps,res = defaultdict(list),[]
    
    for i, size in enumerate(groupSizes):
        grps[size].append(i)
        
        if len(grps[size]) == size:
            res.append(grps[size]); grps[size] = []
            
    return res


assert groupThePeople([3,3,3,3,3,1,3]) == [[0,1,2],[5],[3,4,6]]
assert groupThePeople([2,1,3,3,3,2]) == [[1],[2,3,4],[0,5]]
